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
        mongo_db_admin.py -c file -d path
            {-L [-n dir_path [-p]]} |
            {-R [db_name [db_name2 ...]]} |
            {-C [db_name [db_name2 ...]] [-t table_name [table_name2 ...]]} |
            {-D [db_name [db_name2 ...]] [-t table_name [table_name2 ...]]
                [-f]} |
            {-M [-j [-g]] | [-i db_name:table_name -m config_file] |
                [-o dir_path/file [-a]] | [-z]}
                [-e to_email [to_email2 ...] [-s subject_line] [-u]] |
            {-G {global | rs | startupWarnings} | [-j [-g] | -l] |
                [-o dir_path/file [-a]]} |
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -L => Run a log rotate on the mongo database error log.
            -n dir path => Directory path to where the old mongo database
                error log file will be moved to.
            -p Compress Mongo log after log rotation.

        -R [database name(s)] => Repair database.
            Note 1:  If no database name is provided, then all databases are
                repaired.
            Warning:  This option will not work with Mongo 4.2.0 and above and
                will cause the node to stacktrace.

        -C [database name(s)] => Defrag tables.
            Note: If no db_name is provided, then all database are processed.
                Can use the -t option to specify an individual table.  If no
                -t is used, then all tables in the database are compacted.
            -t table_name(s) => Table names.

        -D [database name(s)] => Validate tables.
            Note: If no db_name is provided, then all database are processed.
                Can use the -t option to specify an individual table.  If no
                -t is used, then all tables in the database are compacted.
            -t table_name(s) => Table names.
            -f => Run full validate scan on table(s).

        -M Display the current database status; uptime, memory use, and usage.
            -j => Return output in JSON format.
            -g => Flatten the JSON data structure to file and standard out.
            -i {database:collection} => Name of database and collection to
                insert the database status data into.
                Default value:  sysmon:mongo_db_status
            -m file => Mongo config file used for the insertion into a Mongo
                database.  Do not include the .py extension.
            -o path/file => Directory path and file name for output.
                Use the -a option to append to an existing file.
                Format compability: JSON and standard out.
            -a => Append output to output file.
            -z => Suppress standard out.
            -e to_email_addresses => Enables emailing capability for an option
                if the option allows it.  Sends output to one or more email
                addresses.  Email addresses are delimited by spaces.
                -s subject_line => Subject line of email.  Optional, will
                    create own subject line if one is not provided.
                -u => Override the default mail command and use mailx.

        -G {global | rs | startupWarnings} => Retrieve the mongo error
            log from mongo memory cache.
            Default value is: global.
            Note:  Options -j and -l are Xor.
            -j => Return output in JSON format.
            -g => Flatten the JSON data structure to file and standard out.
            -l => Return output in "list" format.
            -o path/file => Directory path and file name for output.
                Use the -a option to append to an existing file.
                Format compability: JSON, list, and standard out.
            -a => Append output to output file.

        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  Options -R, -C, -D, and -M are Xor.
        NOTE 2:  Options -M and -G are Xor.
        NOTE 3:  -v and -h overrides all other options.

    Notes:
        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format is for connecting to a Mongo
            database/replica set for monitoring and is also used to connect to
            a Mongo database/replica set for for inserting data into.  Create
            two different configuration files if monitoring one Mongo database
            and inserting into a different Mongo database.

            There are two ways to connect:  single or replica set.

            Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "USER"
            japd = "PSWORD"
            host = "HOST_IP"
            name = "HOSTNAME"
            port = 27017
            conf_file = None
            auth = True
            auth_db = "admin"
            auth_mech = "SCRAM-SHA-1"
            use_arg = True
            use_uri = False

            Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file.  By
                default all these entries are set to None to represent not
                connecting to a replica set.

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

            Note:  If using SSL connections then set one or more of the
                following entries.  This will automatically enable SSL
                connections. Below are the configuration settings for SSL
                connections.  See configuration file for details on each entry:

            ssl_client_ca = None
            ssl_client_key = None
            ssl_client_cert = None
            ssl_client_phrase = None

            Note:  FIPS Environment for Mongo.
              If operating in a FIPS 104-2 environment, this package will
              require at least a minimum of pymongo==3.8.0 or better.  It will
              also require a manual change to the auth.py module in the pymongo
              package.  See below for changes to auth.py.

            - Locate the auth.py file python installed packages on the system
                in the pymongo package directory.
            - Edit the file and locate the "_password_digest" function.
            - In the "_password_digest" function there is an line that should
                match: "md5hash = hashlib.md5()".  Change it to
                "md5hash = hashlib.md5(usedforsecurity=False)".
            - Lastly, it will require the Mongo configuration file entry
                auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Version Issue:  The -R option will fail on Mongodb v4.2.0 and above.  The
        "repairDatabase" command was removed from Mongodb.
        Warning:  Do not run it on a 4.2.0 or better as it will cause the
            database node to stacktrace.

    Example:
        mongo_db_admin.py -c mongo -d config -D sysmon -t mongo_db_status

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
import ast

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import mongo_lib.mongo_libs as mongo_libs
import mongo_lib.mongo_class as mongo_class
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def process_request(server, func_name, db_name=None, tbl_name=None, **kwargs):

    """Function:  process_request

    Description:  Prepares for the type of check based on the arguments passed
        to the function and then calls the "func_name" function.

    Arguments:
        (input) server -> Database server instance.
        (input) func_name -> Name of a function.
        (input) db_name -> List of database names.
        (input) tbl_name -> List of table names.
        (input) **kwargs:
            full -> Full validation table check option.
        (output) err_flag -> True|False - If an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None
    db_name = list() if db_name is None else list(db_name)
    tbl_name = list() if tbl_name is None else list(tbl_name)
    db_list = server.fetch_dbs()

    # Only pass authorization mechanism if present.
    auth_mech = {"auth_mech": server.auth_mech} if hasattr(
        server, "auth_mech") else {}
    mongo = mongo_class.DB(
        server.name, server.user, server.japd, host=server.host,
        port=server.port, db="test", auth=server.auth,
        conf_file=server.conf_file, auth_db=server.auth_db,
        use_arg=server.use_arg, use_uri=server.use_uri, **auth_mech)
    state = mongo.connect()

    if not state[0]:
        err_flag = True
        err_msg = "Connection to Mongo DB:  %s" % state[1]

    else:

        # Process all databases.
        if not db_name:

            for item in db_list:
                func_name(mongo, item, **kwargs)

        # Process all tables in a database.
        elif not tbl_name:

            # Generator builds list of databases to process.
            for dbn in (dbn for dbn in db_name if dbn in db_list):
                func_name(mongo, dbn, **kwargs)

        # Process passed databases and tables.
        else:
            process_dbs_tbls(mongo, func_name, db_name, db_list, tbl_name, **kwargs)

        mongo_libs.disconnect([mongo])

    return err_flag, err_msg


def process_dbs_tbls(mongo, func_name, db_name, db_list, tbl_name, **kwargs):

    """Function:  process_dbs_tbls

    Description:  Process a list of databases and tables.

    Arguments:
        (input) mongo -> Database instance.
        (input) func_name -> Name of a function.
        (input) db_name -> List of database names to check.
        (input) db_list -> List of all databases in Mongo database.
        (input) tbl_name -> List of tables to check.
        (input) **kwargs:
            full -> Full validation table check option.

    """

    db_name = list(db_name)
    db_list = list(db_list)
    tbl_name = list(tbl_name)

    # Generator builds list of databases to process.
    for dbn in (dbn for dbn in db_name if dbn in db_list):
        mongo.chg_db(dbs=dbn)
        tbl_list = mongo.get_tbl_list()
        fnd_tbls = list((tbl for tbl in tbl_name if tbl in tbl_list))

        if fnd_tbls:
            func_name(mongo, dbn, fnd_tbls, **kwargs)

        else:
            print("Found no tables to process in: %s" % (dbn))


def run_dbcc(mongo, db_name, tbl_list=None, **kwargs):

    """Function:  run_dbcc

    Description:  Changes database instance to new database and executes
        validate command against the list of tables.

    Arguments:
        (input) mongo -> Database instance.
        (input) db_name -> Database name.
        (input) tbl_list -> List of tables.
        (input) **kwargs:
            full -> Full validation table check option.

    """

    if tbl_list is None:
        tbl_list = []

    else:
        tbl_list = list(tbl_list)

    mongo.chg_db(dbs=db_name)
    print("DBCC check for %s" % (mongo.db_name))

    if not tbl_list:
        tbl_list = mongo.get_tbl_list()

    for item in tbl_list:
        print("\tChecking table: {0:50}".format(item + "..."), end="")
        status_flag, data = mongo.validate_tbl(item, scan=kwargs.get("full",
                                                                     False))

        if status_flag:
            print("\t%s" % (data["valid"]))

            if data["valid"] is False:
                print("\t\tError: %s" % (data["errors"]))

        else:
            print("\t\tError: %s" % (data))


def dbcc(server, args_array, **kwargs):

    """Function:  dbcc

    Description:  Runs the validate command against one or more tables and can
        also be ran against one or more databases.  The -D and -t
        options will determine which databases and tables are done.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (output) state[0] -> True|False - If an error has occurred.
        (output) state[1] -> Error message.

    """

    args_array = dict(args_array)
    state = process_request(
        server, run_dbcc, args_array["-D"], args_array.get("-t"),
        full=args_array.get("-f", False))

    return state[0], state[1]


def run_compact(mongo, db_name, tbl_list=None, **kwargs):

    """Function:  run_compact

    Description:  Changes database instance to new database and executes
        compact command within the class instance against a list of tables.

    Arguments:
        (input) mongo -> Database instance.
        (input) db_name -> Database name.
        (input) tbl_list -> List of tables.

    """

    tbl_list = list() if tbl_list is None else list(tbl_list)

    mongo.chg_db(dbs=db_name)
    print("Compacting for %s" % (mongo.db_name))

    if not tbl_list:
        tbl_list = mongo.get_tbl_list(False)

    for item in tbl_list:
        print("\tCompacting: {0:50}".format(item + "..."), end="")
        coll = mongo_libs.crt_coll_inst(mongo, db_name, item)
        state = coll.connect()

        if state[0]:
            if coll.coll_options().get("capped", False):
                print("\tCollection capped: not compacted")

            else:

                if mongo.db_cmd("compact", obj=item)["ok"] == 1:
                    print("\tDone")

                else:
                    print("\tCommand Failed")

            mongo_libs.disconnect([coll])

        else:
            print("\tError encountered:  %s" % (state[1]))


def defrag(server, args_array, **kwargs):

    """Function:  defrag

    Description:  Runs the compact command against one or more tables and can
        also be ran against one or more databases.  The -C and -t options
        will determine which databases and tables are done.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (output) err_flag -> True|False - If an error has occurred.
        (output) err_msg -> Error message.

    """

    args_array = dict(args_array)
    data = mongo_class.fetch_ismaster(server)

    if data["ismaster"] and "setName" in data:
        err_flag = True
        err_msg = "Warning: Cannot defrag - database is Primary in ReplicaSet."

    else:
        err_flag, err_msg = process_request(
            server, run_compact, args_array["-C"], args_array.get("-t"))

    return err_flag, err_msg


def run_repair(mongo, db_name, **kwargs):

    """Function:  run_repair

    Description:  Changes database instance to new database and executes the
        repairDatabase command within the class instance.

    Arguments:
        (input) mongo -> Database instance.
        (input) db_name -> Database name.

    """

    mongo.chg_db(dbs=db_name)
    print("Repairing Database: {0:20}".format(db_name + "..."), end="")

    if mongo.db_cmd("repairDatabase")["ok"] == 1:
        print("\tDone")

    else:
        print("\tCommand Failed")


def repair_db(server, args_array, **kwargs):

    """Function:  repair_db

    Description:  Runs the repairDatabase command against one or more databases
        which is determined by -R option from the command line.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (output) state[0] -> True|False - If an error has occurred.
        (output) state[1] -> Error message.

    """

    args_array = dict(args_array)
    state = process_request(server, run_repair, args_array["-R"], None)

    return state[0], state[1]


def status(server, args_array, **kwargs):

    """Function:  status

    Description:  Retrieves a number of database status variables and sends
        them out either in standard out (print) or to a JSON format which
        is printed and/or insert into the database.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            ofile -> file name - Name of output file.
            db_tbl database:table_name -> Mongo database and table name.
            class_cfg -> Mongo Rep Set server configuration.
            mail -> Mail instance.
        (output) err_flag -> True|False - If an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None
    mode = "w"
    indent = 4
    args_array = dict(args_array)
    server.upd_srv_stat()
    outdata = {"Application": "MongoDB",
               "Server": server.name,
               "AsOf": datetime.datetime.strftime(datetime.datetime.now(),
                                                  "%Y-%m-%d %H:%M:%S")}
    outdata.update({"Memory": {"CurrentUsage": server.cur_mem,
                               "MaxUsage": server.max_mem,
                               "PercentUsed": server.prct_mem},
                    "UpTime": server.days_up,
                    "Connections": {"CurrentConnected": server.cur_conn,
                                    "MaxConnections": server.max_conn,
                                    "PercentUsed": server.prct_conn}})

    ofile = kwargs.get("ofile", None)
    mail = kwargs.get("mail", None)
    mongo_cfg = kwargs.get("class_cfg", None)
    db_tbl = kwargs.get("db_tbl", None)

    if args_array.get("-a", False):
        mode = "a"

    if args_array.get("-g", False):
        indent = None

    if "-j" in args_array:
        outdata = json.dumps(outdata, indent=indent)

    if mongo_cfg and db_tbl:
        dbn, tbl = db_tbl.split(":")

        if isinstance(outdata, dict):
            state = mongo_libs.ins_doc(mongo_cfg, dbn, tbl, outdata)

        else:
            state = mongo_libs.ins_doc(mongo_cfg, dbn, tbl,
                                       ast.literal_eval(outdata))

        if not state[0]:
            err_flag = True
            err_msg = "Inserting into Mongo database:  %s" % state[1]

    if ofile and "-j" in args_array:
        gen_libs.write_file(ofile, mode, outdata)

    elif ofile:
        gen_libs.display_data(outdata, f_hdlr=gen_libs.openfile(ofile, mode))

    if mail:
        process_mail(mail, outdata, indent, args_array.get("-u", False))

    if not args_array.get("-z", False):
        gen_libs.display_data(outdata)

    return err_flag, err_msg


def process_mail(mail, data, indent=4, use_mailx=False):

    """Function:  process_mail

    Description:  Add data to mail instance and send mail.

    Arguments:
        (input) mail -> Mail instance.
        (input) data -> Email message data.
        (input) indent -> Spacing for JSON document.
        (input) use_mailx -> True|False - To use the mailx command.

    """

    if isinstance(data, dict):
        mail.add_2_msg(json.dumps(data, indent=indent))

    else:
        mail.add_2_msg(data)

    mail.send_mail(use_mailx=use_mailx)


def rotate(server, args_array, **kwargs):

    """Function:  rotate

    Description:  Initiates a rotate log command and moves log to another
        directory if requested.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (output) err_flag -> True|False - if an error has occurred.
        (output) err_msg -> Error message.

    """

    args_array = dict(args_array)
    err_flag = False
    err_msg = None

    if "-n" in args_array:

        status_flag, msg = gen_libs.chk_crt_dir(args_array["-n"], write=True)

        if status_flag:

            # Pull the log and path from Mongo.
            path_log = \
                mongo_class.fetch_cmd_line(server)[
                    "parsed"]["systemLog"]["path"]
            dir_path = os.path.dirname(path_log)
            mdb_log = os.path.basename(path_log)

            # Pre-list of log files before logRotate.
            pre_logs = gen_libs.dir_file_match(dir_path, mdb_log)
            server.adm_cmd("logRotate")

            # Post-list of log files after logRotate.
            post_logs = gen_libs.dir_file_match(dir_path, mdb_log)
            diff_list = gen_libs.is_missing_lists(post_logs, pre_logs)

            if len(diff_list) > 1:
                err_flag = True
                err_msg = ("Error:  Too many files to move: %s" % (diff_list))

            else:
                gen_libs.mv_file(diff_list[0], dir_path, args_array["-n"])

                if "-p" in args_array:
                    gen_libs.compress(os.path.join(args_array["-n"],
                                                   diff_list[0]))

        else:
            err_flag = True
            err_msg = msg

    else:
        server.adm_cmd("logRotate")

    return err_flag, err_msg


def get_log(server, args_array, **kwargs):

    """Function:  get_log

    Description:  Retrieve the mongo error log from the mongo database cache
        and send to output.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            ofile -> file name - Name of output file.
        (output) err_flag -> True|False - if an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None
    mode = "w"
    indent = 4
    args_array = dict(args_array)

    if args_array.get("-a", False):
        mode = "a"

    if args_array.get("-g", False):
        indent = None

    # Get log data from mongodb.
    data = server.adm_cmd("getLog", arg1=args_array["-G"])
    data["Server"] = server.name
    data["AsOf"] = gen_libs.get_date() + " " + gen_libs.get_time()

    if "-j" in args_array:
        gen_libs.print_data(json.dumps(data, indent=indent), mode=mode,
                            **kwargs)

    elif "-l" in args_array:
        gen_libs.print_data(data["log"], mode=mode, **kwargs)

    else:
        if kwargs.get("ofile", None):
            f_hldr = open(kwargs.get("ofile"), mode)

        else:
            f_hldr = sys.stdout

        for item in data["log"]:
            gen_libs.write_file2(f_hldr, item)

        if kwargs.get("ofile", None):
            f_hldr.close()

    return err_flag, err_msg


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    server = mongo_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mongo_class.Server)
    state = server.connect()

    if state[0]:
        outfile = args_array.get("-o", None)
        db_tbl = args_array.get("-i", None)
        repcfg = None
        mail = None

        if args_array.get("-m", None):
            repcfg = gen_libs.load_module(args_array["-m"], args_array["-d"])

        if args_array.get("-e", None):
            mail = gen_class.setup_mail(args_array.get("-e"),
                                        subj=args_array.get("-s", None))

        # Call function(s) - intersection of command line and function dict.
        for item in set(args_array.keys()) & set(func_dict.keys()):
            err_flag, err_msg = func_dict[item](
                server, args_array, ofile=outfile, db_tbl=db_tbl,
                class_cfg=repcfg, mail=mail, **kwargs)

            if err_flag:
                print("Error:  %s" % (err_msg))
                break

        mongo_libs.disconnect([server])

    else:
        print("Connection failure:  %s" % (state[1]))


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

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-d", "-n"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-C": defrag, "-D": dbcc, "-R": repair_db, "-M": status,
                 "-L": rotate, "-G": get_log}
    opt_con_req_dict = {"-j": ["-M", "-G"]}
    opt_con_req_list = {"-i": ["-m"], "-n": ["-L"], "-l": ["-G"], "-f": ["-D"],
                        "-s": ["-e"], "-u": ["-e"]}
    opt_def_dict = {"-C": [], "-D": [], "-R": [], "-G": "global",
                    "-i": "sysmon:mongo_db_status"}
    opt_multi_list = ["-C", "-D", "-R", "-t", "-e", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-t", "-C", "-D", "-R", "-i", "-m", "-o",
                    "-G", "-n", "-e", "-s", "-y"]
    opt_valid_val = {"-G": ["global", "rs", "startupWarnings"]}
    opt_xor_dict = {"-R": ["-C", "-M", "-D"], "-C": ["-D", "-M", "-R"],
                    "-D": ["-C", "-M", "-R"], "-M": ["-C", "-D", "-R", "-G"],
                    "-G": ["-M"], "-j": ["-l"], "-l": ["-j"]}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list,
                                       opt_def_dict, multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_valid_val(args_array, opt_valid_val) \
       and arg_parser.arg_xor_dict(args_array, opt_xor_dict) \
       and arg_parser.arg_cond_req_or(args_array, opt_con_req_dict) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                       file_crt_list):

        try:
            prog_lock = gen_class.ProgramLock(cmdline.argv,
                                              args_array.get("-y", ""))
            run_program(args_array, func_dict)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("WARNING:  lock in place for mongo_db_admin with id of: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())
