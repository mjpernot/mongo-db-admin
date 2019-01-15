#!/usr/bin/python
# Classification (U)

"""Program:  mongo_db_admin.py

    Description:  A Mongo Database Administration program that can run a number
        of different administration functions such as repairing a database,
        compacting/defraging tables or entire database, or validating
        tables in a database.  Can return the database's status to
        include uptime, connection usage, and memory use and can also
        retrieve the Mongo error log that currently resides in memory.

    Usage:
        mongo_db_admin.py -c file -d path -L [-n dir_path] |
            {-R [db_name [db_name ...]]} |
            {-C [db_name [db_name ...]] [-t table_name [table_name ...]]} |
            {-D [db_name [db_name ...]] [-t table_name [table_name ...]]} |
            [-f] {-M {-j | -i db_name:table_name |
            -m file | -o dir_path/file}} |
            {-G {global | rs | startupWarnings} | {-j | -l | -o dir_path/file}}
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -R [database name(s)] => Repair database.  If no db_name is
            provided, then all databases are repaired.
        -C [database name(s)] => Defrag tables.  Can be used in
            conjunction with the -t option to specify an individual
            table.  If no -t is used, then all tables in the database
            are compacted.  If no db_name is provided, then all
            database are processed.
        -D [database name(s)] => Validate tables. Can be used in conjunction
            with the -t option to specify an individual table.  If no -t is
            used, then all tables in the database are validated.  If no
            db_name is provided, then all database are processed.  Also used
            in conjunction with the -f option.
        -f => Run full validate scan on table(s).  For -D option only.
        -M Display the current database status, such as uptime, memory
            use, and connection usage.  Can use the following options:
            -m, -j, -i, and -o.
        -j => Return output in JSON format.  For -G and -M options.
        -l => Return output in "list" format.  For -G option.
        -i {database:collection} => Name of database and collection to insert
            the database status data into.  Delimited by colon (:).
            Default: sysmon:mongo_db_status  When using this option, the
            configuration file format will determine whether the connection
            will be to a single Mongo database server or to a Mongo replica
            set.  See Configuration File format below on each format.
        -m file => Mongo config file used for the insertion into a Mongo
            database.  Do not include the .py extension.  Used only with the
            -i option.
        -o path/file => Directory path and file name for output.  Can be
            used with -M or -G options.  Format compability:
                -M option => JSON and standard out.
                -G option => JSON, list, and standard out.
        -t table_name(s) => Table names.  Used with the -C or -D options.
        -L => Run a log rotate on the mongo database error log.
        -n dir path => Directory path to where the old mongo database
            error log file will be moved to.
        -G {global | rs | startupWarnings} => Retrieve the mongo error
            log from mongo memory cache.  Default value is: global.  Can
            use the following options:  -j or -l and -o.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  Options -R, -C, -D, and -M are XOR.
        NOTE 2:  Options -M and -G are XOR.
        NOTE 3:  -v and -h overrides all other options.
        NOTE 4:  Options -j and -l are XOR.

    Notes:
        Mongo configuration file format (mongo.py).  The configuration
            file format for the Mongo connection used for inserting data into
            a database.  There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 27017)
            conf_file = None
            auth = True

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Known Bug:  For options -C and -D.  If multiple database values are passed
        to the program and the -t option is used.  If one of the
        databases has no tables in the table listed presented, then all
        of the tables within the database will be processed.

    Known Bug:  The -i option does not work for the -M option if the -j option
        is not selected also.  It will only display the output to
        standard out in standard format and will not insert into the database.
        Workaround:  Use -j option whenever using -i option.

    Example:
        mongo_db_admin.py -c mongo -d config -D admin -t system.users

"""


# Libraries and Global Variables

# Standard
# For Python 2.6/2.7: Redirection of stdout in a print command.
from __future__ import print_function
import sys
import datetime
import os

# Third party
import json

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.cmds_gen as cmds_gen
import mongo_lib.mongo_libs as mongo_libs
import mongo_lib.mongo_class as mongo_class
import version

# Version
__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def process_request(SERVER, func_name, db_name=None, tbl_name=None, **kwargs):

    """Function:  process_request

    Description:  Prepares for the type of check based on the arguments passed
        to the function and then calls the "func_name" function.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) func_name -> Name of a function.
        (input) db_name -> Database name or 'all'
        (input) tbl_name -> List of table names.
        (input) **kwargs:
            full -> Full validation table check option.

    """

    if db_name is None:
        db_name = []

    if tbl_name is None:
        tbl_name = []

    db_list = SERVER.fetch_dbs()

    DB = mongo_class.DB(SERVER.name, SERVER.user, SERVER.passwd, SERVER.host,
                        SERVER.port, "test", SERVER.auth, SERVER.conf_file)
    DB.connect()

    # Process all databases.
    if not db_name:

        for x in db_list:
            func_name(DB, x, **kwargs)

    # Process all tables in a database.
    elif not tbl_name:

        # Generator builds list of databases to process.
        for db in (db for db in db_name if db in db_list):
            func_name(DB, db, **kwargs)

    # Process passed databases and tables.
    else:
        # Generator builds list of databases to process.
        for db in (db for db in db_name if db in db_list):
            DB.chg_db(db=db)
            tbl_list = DB.get_tbl_list()

            # Generator builds list of tables.
            func_name(DB, db,
                      list((tbl for tbl in tbl_name if tbl in tbl_list)),
                      **kwargs)

    cmds_gen.disconnect([DB])


def run_dbcc(DB, db_name, tbl_list=None, **kwargs):

    """Function:  run_dbcc

    Description:  Changes database instance to new database and executes
        validate command against the list of tables.

    Arguments:
        (input) DB -> Database instance.
        (input) db_name -> Database name.
        (input) tbl_list -> List of tables.
        (input) **kwargs:
            full -> Full validation table check option.

    """

    if tbl_list is None:
        tbl_list = []

    DB.chg_db(db=db_name)
    print("DBCC check for %s" % (DB.db_name))

    if not tbl_list:
        tbl_list = DB.get_tbl_list()

    for x in tbl_list:
        print("\tChecking table: {0:50}".format(x + "..."), end="")

        data = DB.validate_tbl(x, scan=kwargs.get("full", False))

        print("\t%s" % (data["valid"]))

        if data["valid"] is False:
            print("\t\tError: %s" % (data["errors"]))


def dbcc(SERVER, args_array, **kwargs):

    """Function:  dbcc

    Description:  Runs the validate command against one or more tables and can
        also be ran against one or more databases.  The -D and -t
        options will determine which databases and tables are done.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            None
        (output) False - if an error has occurred.
        (output) None -> Error message.

    """

    process_request(SERVER, run_dbcc, args_array["-D"], args_array.get("-t"),
                    full=args_array.get("-f", False))

    return False, None


def run_compact(DB, db_name, tbl_list=None):

    """Function:  run_compact

    Description:  Changes database instance to new database and executes
        compact command within the class instance against a list of tables.

    Arguments:
        (input) DB -> Database instance.
        (input) db_name -> Database name.
        (input) tbl_list -> List of tables.

    """

    if tbl_list is None:
        tbl_list = []

    DB.chg_db(db=db_name)
    print("Compacting for %s" % (DB.db_name))

    if not tbl_list:
        tbl_list = DB.get_tbl_list(False)

    for x in tbl_list:
        print("\tCompacting: {0:50}".format(x + "..."), end="")

        COLL = mongo_libs.crt_coll_inst(DB, db_name, x)
        COLL.connect()

        if COLL.coll_options().get("capped", False):
            print("\tCollection capped: not compacted")

        else:

            if DB.db_cmd("compact", obj=x)["ok"] == 1:
                print("\tDone")

            else:
                print("\tCommand Failed")

        cmds_gen.disconnect([COLL])


def defrag(SERVER, args_array, **kwargs):

    """Function:  defrag

    Description:  Runs the compact command against one or more tables and can
        also be ran against one or more databases.  The -C and -t options
        will determine which databases and tables are done.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            None
        (output) err_flag -> True|False - if an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None

    data = mongo_class.fetch_ismaster(SERVER)

    # Primary servers not allowed to be defragged.
    if data["ismaster"] and "setName" in data:
        err_flag = True
        err_msg = "Error:  Primary in a Replica Set and cannot be defragged."

    else:
        process_request(SERVER, run_compact, args_array["-C"],
                        args_array.get("-t"))

    return err_flag, err_msg


def run_repair(DB, db_name):

    """Function:  run_repair

    Description:  Changes database instance to new database and executes the
        repairDatabase command within the class instance.

    Arguments:
        (input) DB -> Database instance.
        (input) db_name -> Database name.

    """

    DB.chg_db(db=db_name)
    print("Repairing Database: {0:20}".format(db_name + "..."), end="")

    if DB.db_cmd("repairDatabase")["ok"] == 1:
        print("\tDone")

    else:
        print("\tCommand Failed")


def repair_db(SERVER, args_array, **kwargs):

    """Function:  repair_db

    Description:  Runs the repairDatabase command against one or more databases
        which is determined by -R option from the command line.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            None
        (output) False - if an error has occurred.
        (output) None -> Error message.

    """

    process_request(SERVER, run_repair, args_array["-R"], None)

    return False, None


def status(SERVER, args_array, **kwargs):

    """Function:  status

    Description:  Retrieves a number of database status variables and sends
        them out either in standard out (print) or to a JSON format which
        is printed and/or insert into the database.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            ofile -> file name - Name of output file.
            db_tbl database:table_name -> Mongo database and table name.
            class_cfg -> Mongo Rep Set server configuration.
        (output) False - if an error has occurred.
        (output) None -> Error message.

    """

    SERVER.upd_srv_stat()

    outdata = {"Application": "Mongo Database",
               "Server": SERVER.name,
               "Asof": datetime.datetime.strftime(datetime.datetime.now(),
                                                  "%Y-%m-%d %H:%M:%S")}

    outdata.update({"Memory": {"Current_Usage": SERVER.cur_mem,
                               "Max_Usage": SERVER.max_mem,
                               "Percent_Used": SERVER.prct_mem},
                    "Uptime": SERVER.days_up,
                    "Connections": {"Current_Connected": SERVER.cur_conn,
                                    "Max_Connections": SERVER.max_conn,
                                    "Percent_Used": SERVER.prct_conn}})

    if "-j" in args_array:
        mongo_libs.json_prt_ins_2_db(outdata, **kwargs)

    else:
        if kwargs.get("ofile", None):
            gen_libs.print_dict(outdata, no_std=True, **kwargs)

        else:
            gen_libs.display_data(outdata)

    return False, None


def rotate(SERVER, args_array, **kwargs):

    """Function:  rotate

    Description:  Initiates a rotate log command and moves log to another
        directory if requested.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            None
        (output) err_flag -> True|False - if an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None

    if "-n" in args_array:

        status, msg = gen_libs.chk_crt_dir(args_array["-n"], write=True)

        if status:

            # Pull the log and path from Mongodb.
            path_log = \
                mongo_class.fetch_cmd_line(SERVER)[
                    "parsed"]["systemLog"]["path"]
            dir_path = os.path.dirname(path_log)
            mdb_log = os.path.basename(path_log)

            # Pre list of log files before logRotate.
            pre_logs = gen_libs.dir_file_match(dir_path, mdb_log)

            SERVER.adm_cmd("logRotate")

            # Post list of log files after logRotate.
            post_logs = gen_libs.dir_file_match(dir_path, mdb_log)

            diff_list = gen_libs.is_missing_lists(post_logs, pre_logs)

            if len(diff_list) > 1:
                err_flag = True
                err_msg = ("Error:  Too many files to move: %s" % (diff_list))

            else:
                gen_libs.mv_file(diff_list[0], dir_path, args_array["-n"])

        else:
            err_flag = True
            err_msg = msg

    else:
        SERVER.adm_cmd("logRotate")

    return err_flag, err_msg


def get_log(SERVER, args_array, **kwargs):

    """Function:  get_log

    Description:  Retrieve the mongo error log from the mongo database cache
        and send to output.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            ofile -> file name - Name of output file.
        (output) False - if an error has occurred.
        (output) None -> Error message.

    """

    # Get log data from mongodb.
    data = SERVER.adm_cmd("getLog", arg1=args_array["-G"])

    if "-j" in args_array:
        gen_libs.print_data(json.dumps(data, indent=4), **kwargs)

    elif "-l" in args_array:
        gen_libs.print_data(data["log"], **kwargs)

    else:
        if kwargs.get("ofile", None):
            f_hldr = open(kwargs.get("ofile"), "w")

        else:
            f_hldr = sys.stdout

        for x in data["log"]:
            gen_libs.write_file2(f_hldr, x)

        if kwargs.get("ofile", None):
            f_hldr.close()

    return False, None


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.
        (input) **kwargs:
            multi_val -> List of options that may have multiple values.

    """

    SERVER = mongo_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mongo_class.Server)
    SERVER.connect()

    outfile = args_array.get("-o", None)
    db_tbl = args_array.get("-i", None)

    Rep_Cfg = None
    if args_array.get("-m", None):
        Rep_Cfg = gen_libs.load_module(args_array["-m"], args_array["-d"])

    # Call function(s) - intersection of command line and function dict.
    for x in set(args_array.keys()) & set(func_dict.keys()):
        err_flag, err_msg = func_dict[x](SERVER, args_array, ofile=outfile,
                                         db_tbl=db_tbl, class_cfg=Rep_Cfg,
                                         **kwargs)

        if err_flag:
            cmds_gen.disconnect([SERVER])
            sys.exit(err_msg)

    cmds_gen.disconnect([SERVER])


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        file_chk_list -> contains the options which will have files included.
        file_crt_list -> contains options which require files to be created.
        func_dict -> dictionary list for the function calls or other options.
        opt_arg_list -> contains optional arguments for the command line.
        opt_con_req_dict -> contains options requiring one or more options.
        opt_con_req_list -> contains the options that require other options.
        opt_def_dict -> contains options with their default values.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        opt_valid_val -> contains a list of valid values for options.
        opt_xor_dict -> contains dict with key that is xor with it's values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-d", "-n"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-C": defrag, "-D": dbcc, "-R": repair_db, "-M": status,
                 "-L": rotate, "-G": get_log}
    opt_con_req_dict = {"-j": ["-M", "-G"]}
    opt_con_req_list = {"-i": ["-m"], "-n": ["-L"], "-l": ["-G"], "-f": ["-D"]}
    opt_def_dict = {"-C": [], "-D": [], "-R": [], "-G": "global",
                    "-i": "sysmon:mongo_db_status"}
    opt_multi_list = ["-C", "-D", "-R", "-t"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-t", "-C", "-D", "-R", "-i", "-m", "-o",
                    "-G", "-n"]
    opt_valid_val = {"-G": ["global", "rs", "startupWarnings"]}
    opt_xor_dict = {"-R": ["-C", "-M", "-D"], "-C": ["-D", "-M", "-R"],
                    "-D": ["-C", "-M", "-R"], "-M": ["-C", "-D", "-R", "-G"],
                    "-G": ["-M"], "-j": ["-l"], "-l": ["-j"]}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list, opt_def_dict,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message):
        if not arg_parser.arg_require(args_array, opt_req_list) \
           and arg_parser.arg_valid_val(args_array, opt_valid_val) \
           and arg_parser.arg_xor_dict(args_array, opt_xor_dict) \
           and arg_parser.arg_cond_req_or(args_array, opt_con_req_dict) \
           and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
           and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
           and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                           file_crt_list):

            run_program(args_array, func_dict)


if __name__ == "__main__":
    sys.exit(main())