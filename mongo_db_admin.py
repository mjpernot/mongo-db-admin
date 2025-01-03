#!/usr/bin/python
# Classification (U)

"""Program:  mongo_db_admin.py

    Description:  A Mongo Database Administration program that can run a number
        of different administration functions such as compacting/defraging
        tables or entire database, or validating tables in a database.  Can
        return the database's status to include uptime, connection usage, and
        memory use and can also retrieve the Mongo error log that currently
        resides in memory.

    Usage:
        mongo_db_admin.py -c file -d path
            {-L [-n dir_path [-p]]} |
            {-C [db_name [db_name2 ...]] [-t table_name [table_name2 ...]]
                [-m config_file -i [db_name:table_name]]
                [-o dir_path/file [-w a|w]] [-z] [-r [-k N]]
                [-e to_email [to_email2 ...] [-s subject_line] [-u]]} |
            {-D [db_name [db_name2 ...]] [-t table_name [table_name2 ...]]
                [-f] [-m config_file -i [db_name:table_name]]
                [-o dir_path/file [-w a|w]] [-z] [-r [-k N]]
                [-e to_email [to_email2 ...] [-s subject_line] [-u]]} |
            {-M [-m config_file -i [db_name:table_name]]
                [-o dir_path/file [-w a|w]] [-z] [-r [-k N]]
                [-e to_email [to_email2 ...] [-s subject_line] [-u]]} |
            {-G {global | rs | startupWarnings}
                [-m config_file -i [db_name:table_name]]
                [-o dir_path/file [-w a|w]] [-z] [-r [-k N]]
                [-e to_email [to_email2 ...] [-s subject_line] [-u]]} |
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -L => Run a log rotate on the mongo database error log.
            Default:  Truncate the log without copying it.
            -n dir path => Directory path to where the old mongo database
                error log file will be copied to before being truncated.
            -p => Compress Mongo log after log rotation.

        -C [database name(s)] => Defrag tables.
            Note: If no db_name is provided, then all database are processed.
                Can use the -t option to specify an individual table.  If no
                -t is used, then all tables in the database are compacted.
            -t table name(s) => Table names to defrag.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mongo_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -D [database name(s)] => Validate tables.
            Note: If no db_name is provided, then all database are processed.
                Can use the -t option to specify an individual table.  If no
                -t is used, then all tables in the database are compacted.
            -t table name(s) => Table names to validate.
            -f => Run full validate scan on table(s).
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mongo_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -M Display the current database status; uptime, memory use, and usage.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mongo_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -G {global | rs | startupWarnings} => Retrieve the mongo error
            log from mongo memory cache.
            Default value is: global.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mongo_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  Options -L, -C, -D, and -M are Xor.
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

            Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file.  By
                default all these entries are set to None to represent not
                connecting to a replica set.

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

            If Mongo is set to use TLS or SSL connections, then one or more of
            the following entries will need to be completed to connect using
            TLS or SSL protocols.
                Note:  Read the configuration file to determine which entries
                will need to be set.

            SSL:
                auth_type = None
                ssl_client_ca = None
                ssl_client_key = None
                ssl_client_cert = None
                ssl_client_phrase = None
            TLS:
                auth_type = None
                tls_ca_certs = None
                tls_certkey = None
                tls_certkey_phrase = None

            Databases to ignore.
            NOTE: The default list of databases are the system databases
                (admin, config, local) and should be skipped for some options.
            ign_dbs = ["admin", "config", "local"]

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

    Example:
        mongo_db_admin.py -c mongo -d config -D sysmon -t mongo_db_status

"""


# Libraries and Global Variables

# Standard
import sys
import datetime
import os
import json
import pprint

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .mongo_lib import mongo_libs
    from .mongo_lib import mongo_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import mongo_lib.mongo_libs as mongo_libs           # pylint:disable=R0402
    import mongo_lib.mongo_class as mongo_class         # pylint:disable=R0402
    import version

__version__ = version.__version__

# Global
SYS_DBS = ["admin", "config", "local"]


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def get_all_dbs_tbls(server, db_list, **kwargs):

    """Function:  get_all_dbs_tbls

    Description:  Return a dictionary of databases with table lists.

    Arguments:
        (input) server -> Server instance
        (input) db_list -> List of database names
        (input) kwargs:
            ign_db_tbl -> Database dictionary with list of tables to ignore
        (output) db_dict -> Dictionary of databases and lists of tables

    """

    db_dict = {}
    db_list = list(db_list)
    ign_db_tbl = dict(kwargs.get("ign_db_tbl", {}))

    for dbs in db_list:
        ign_tbls = ign_db_tbl[dbs] if dbs in ign_db_tbl else []
        server.chg_db(dbs=dbs)
        tbl_list = gen_libs.del_not_and_list(
            server.get_tbl_list(inc_sys=False), ign_tbls)
        db_dict[dbs] = tbl_list

    return db_dict


def get_db_tbl(server, db_list, **kwargs):

    """Function:  get_db_tbl

    Description:  Determines which databases and tables will be checked.

    Arguments:
        (input) server -> Mongo DB instance
        (input) db_list -> List of database names
        (input) **kwargs:
            ign_dbs -> List of databases to skip
            tbls -> List of tables to process
            ign_db_tbl -> Database dictionary with list of tables to ignore
        (output) db_dict -> Dictionary of databases and lists of tables

    """

    db_dict = {}
    db_list = list(db_list)
    ign_dbs = list(kwargs.get("ign_dbs", []))
    tbls = kwargs.get("tbls", [])
    ign_db_tbl = dict(kwargs.get("ign_db_tbl", {}))

    if db_list:
        db_list = gen_libs.del_not_and_list(db_list, ign_dbs)

        if len(db_list) == 1 and tbls:
            server.chg_db(dbs=db_list[0])
            tbl_list = gen_libs.del_not_in_list(
                tbls, server.get_tbl_list(inc_sys=False))
            ign_tbls = \
                ign_db_tbl[db_list[0]] if db_list[0] in ign_db_tbl else []
            tbl_list = gen_libs.del_not_and_list(tbl_list, ign_tbls)
            db_dict[db_list[0]] = tbl_list

        elif db_list:
            db_dict = get_all_dbs_tbls(server, db_list, ign_db_tbl=ign_db_tbl)

        else:
            print("get_db_tbl 1: Warning:  No databases to process")

    else:
        db_list = server.fetch_dbs()
        db_list = gen_libs.del_not_and_list(db_list, ign_dbs)

        if db_list:
            db_dict = get_all_dbs_tbls(server, db_list, ign_db_tbl=ign_db_tbl)

        else:
            print("get_db_tbl 2: Warning:  No databases to process")

    return db_dict


def get_json_template(server):

    """Function:  get_json_template

    Description:  Return a JSON template format.

    Arguments:
        (input) server -> Server instance
        (output) json_doc -> JSON filled-in template document

    """

    json_doc = {}
    json_doc["Platform"] = "Mongo"
    json_doc["Server"] = server.name
    json_doc["AsOf"] = gen_libs.get_date() + "T" + gen_libs.get_time()

    return json_doc


def create_data_config(args):

    """Function:  create_data_config

    Description:  Create data_out config parameters.

    Arguments:
        (input) args -> ArgParser class instance
        (output) data_config -> Dictionary for data_out config parameters

    """

    data_config = {}
    data_config["to_addr"] = args.get_val("-e")
    data_config["subj"] = args.get_val("-s")
    data_config["mailx"] = args.get_val("-u", def_val=False)
    data_config["outfile"] = args.get_val("-o")
    data_config["mode"] = args.get_val("-w", def_val="w")
    data_config["expand"] = args.get_val("-r", def_val=False)
    data_config["indent"] = args.get_val("-k")
    data_config["suppress"] = args.get_val("-z", def_val=False)
    data_config["db_tbl"] = args.get_val("-i")

    if args.get_val("-m", def_val=False):
        data_config["mongo"] = gen_libs.load_module(
            args.get_val("-m"), args.get_val("-d"))

    return data_config


def data_out(data, **kwargs):

    """Function:  data_out

    Description:  Outputs the data in a variety of formats and media.

    Arguments:
        (input) data -> JSON data document
        (input) kwargs:
            to_addr -> To email address
            subj -> Email subject line
            mailx -> True|False - Use mailx command
            outfile -> Name of output file name
            mode -> w|a => Write or append mode for file
            expand -> True|False - Expand the JSON format
            indent -> Indentation of JSON document if expanded
            suppress -> True|False - Suppress standard out
            mongo -> Mongo config file - Insert into Mongo database
            db_tbl -> database:table - Database name:Table name
        (output) state -> True|False - Successful operation
        (output) msg -> None or error message

    """

    state = True
    msg = None

    if not isinstance(data, dict):
        return False, f"Error: Is not a dictionary: {data}"

    mail = None
    data = dict(data)
    cfg = {"indent": kwargs.get("indent", 4)} if kwargs.get("indent", False) \
        else {}

    if kwargs.get("to_addr", False):
        subj = kwargs.get("subj", "Mongo_db_admin_NoSubjectLine")
        mail = gen_class.setup_mail(kwargs.get("to_addr"), subj=subj)
        mail.add_2_msg(json.dumps(data, **cfg))
        mail.send_mail(use_mailx=kwargs.get("mailx", False))

    if kwargs.get("outfile", False):
        with open(kwargs.get("outfile"), mode=kwargs.get("mode", "w"),
                  encoding="UTF-8") as ofile:
            pprint.pprint(data, stream=ofile, **cfg)

    if not kwargs.get("suppress", False):
        if kwargs.get("expand", False):
            pprint.pprint(data, **cfg)

        else:
            print(data)

    if kwargs.get("mongo", False):
        dbs, tbl = kwargs.get("db_tbl").split(":")
        state, msg = mongo_libs.ins_doc(kwargs.get("mongo"), dbs, tbl, data)

    return state, msg


def dbcc(server, args):                         # pylint:disable=R0914,W0613

    """Function:  dbcc

    Description:  Runs the validate command against one or more tables and
        against one or more databases.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (output) status -> Success of command: (True|False, Error Message)

    """

    global SYS_DBS                                      # pylint:disable=W0602

    status = (True, None)

    mongo = mongo_libs.create_instance(
        args.get_val("-c"), args.get_val("-d"), mongo_class.DB)
    state = mongo.connect()

    if not state[0]:
        status = (False, f"Connection to Mongo DB:  {state[1]}")

    else:
        db_list = args.get_val("-D", def_val=[])
        tbls = args.get_val("-t", def_val=[])
        cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
        ign_dbs = cfg.ign_dbs if hasattr(cfg, "ign_dbs") else SYS_DBS
        db_dict = get_db_tbl(mongo, db_list, tbls=tbls, ign_dbs=ign_dbs)
        results = get_json_template(mongo)
        results["Type"] = "validate"
        results["Results"] = []
        data_config = dict(create_data_config(args))

        for dbn in db_dict.items():
            mongo.chg_db(dbs=dbn[0])
            t_results = {"Database": dbn[0], "Tables": []}

            for tbl in dbn[1]:
                t_data = {"TableName": tbl}
                data = mongo.validate_tbl(tbl, scan=args.arg_exist("-f"))

                if data[0]:
                    t_data["Status"] = data[1]["valid"]

                    if not data[1]["valid"]:
                        t_data["Message"] = data[1]["errors"]

                else:
                    t_data["Status"] = f"Error encountered:  {data[1]}"

                t_results["Tables"].append(t_data)

            results["Results"].append(t_results)

        mongo_libs.disconnect([mongo])
        state = data_out(results, **data_config)

        if not state[0]:
            status = (state[0], f"dbcc: Error encountered: {state[1]}")

    return status


def compact(mongo, coll, tbl):

    """Function:  compact

    Description:  Runs the compact command and checks the status return.

    Arguments:
        (input) mongo -> Database instance
        (input) coll -> Database collection instance
        (input) tbl -> Table name
        (output) status -> Status of compact command

    """

    if coll.coll_options().get("capped", False):
        status = "Collection capped: not compacted"

    else:

        if mongo.db_cmd("compact", obj=tbl)["ok"] == 1:
            status = "Compact Done"

        else:
            status = "Compact Failed"

    return status


def defrag(server, args):                               # pylint:disable=R0914

    """Function:  defrag

    Description:  Runs the compact command against one or more tables and
        against one or more databases.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (output) status -> Success of command: (True|False, Error Message)

    """

    global SYS_DBS                                      # pylint:disable=W0602

    status = (True, None)
    data = mongo_class.fetch_ismaster(server)

    if data["ismaster"] and "setName" in data:
        status = (False, "Warning: Cannot defrag the Master in a ReplicaSet.")

    else:
        mongo = mongo_libs.create_instance(
            args.get_val("-c"), args.get_val("-d"), mongo_class.DB)
        state = mongo.connect()

        if not state[0]:
            status = (False, f"Connection to Mongo DB:  {state[1]}")

        else:
            db_list = args.get_val("-C", def_val=[])
            tbls = args.get_val("-t", def_val=[])
            cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
            ign_dbs = cfg.ign_dbs if hasattr(cfg, "ign_dbs") else SYS_DBS
            db_dict = get_db_tbl(mongo, db_list, tbls=tbls, ign_dbs=ign_dbs)
            results = get_json_template(mongo)
            results["Type"] = "defrag"
            results["Results"] = []
            data_config = dict(create_data_config(args))

            for dbn in db_dict.items():
                mongo.chg_db(dbs=dbn[0])
                t_results = {"Database": dbn[0], "Tables": []}

                for tbl in dbn[1]:
                    coll = mongo_libs.crt_coll_inst(mongo, dbn[0], tbl)
                    state = coll.connect()
                    t_data = {"TableName": tbl}

                    if state[0]:
                        t_data["Status"] = compact(mongo, coll, tbl)
                        mongo_libs.disconnect([coll])

                    else:
                        t_data["Status"] = f"Error encountered:  {state[1]}"

                    t_results["Tables"].append(t_data)

                results["Results"].append(t_results)

            mongo_libs.disconnect([mongo])
            state = data_out(results, **data_config)

            if not state[0]:
                status = (False, f"defrag: Error encountered: {state[1]}")

    return status


def get_status(server, args):

    """Function:  get_status

    Description:  Retrieves a number of database status variables and sends
        them out either in standard out (print) or to a JSON format which
        is printed and/or insert into the database.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (output) status -> Success of command: (True|False, Error Message)

    """

    status = (True, None)
    server.upd_srv_stat()
    results = get_json_template(server)
    results["Type"] = "status"
    results["Application"] = "MongoDB"
    results["AsOf"] = datetime.datetime.strftime(
        datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    results["Memory"] = {
        "CurrentUsage": server.cur_mem, "MaxUsage": server.max_mem,
        "PercentUsed": server.prct_mem}
    results["UpTime"] = server.days_up
    results["Connections"] = {
        "CurrentConnected": server.cur_conn, "MaxConnections": server.max_conn,
        "PercentUsed": server.prct_conn}
    data_config = dict(create_data_config(args))
    state = data_out(results, **data_config)

    if not state[0]:
        status = (False, f"status: Error encountered: {state[1]}")

    return status


def rotate(server, args):

    """Function:  rotate

    Description:  Initiates a rotate log command and moves log to another
        directory if requested.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (output) status -> Success of command: (True|False, Error Message)

    """

    status = (True, None)

    if args.arg_exist("-n"):

        status_flag, msg = gen_libs.chk_crt_dir(args.get_val("-n"), write=True)

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
                status = (
                    False, f"Error:  Too many files to move: {diff_list}")

            else:
                gen_libs.mv_file(diff_list[0], dir_path, args.get_val("-n"))

                if args.arg_exist("-p"):
                    gen_libs.compress(
                        os.path.join(args.get_val("-n"), diff_list[0]))

        else:
            status = (False, msg)

    else:
        server.adm_cmd("logRotate")

    return status


def get_log(server, args):

    """Function:  get_log

    Description:  Retrieve the mongo error log from the mongo database cache
        and send to output.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (output) status -> Success of command: (True|False, Error Message)

    """

    status = (True, None)
    results = get_json_template(server)
    results["Type"] = "status"
    data = server.adm_cmd("getLog", arg1=args.get_val("-G"))
    results = gen_libs.merge_two_dicts(results, data)[0]
    data_config = dict(create_data_config(args))
    state = data_out(results, **data_config)

    if not state[0]:
        status = (False, f"get_log: Error encountered: {state[1]}")

    return status


def run_program(args, func_dict):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options

    """

    func_dict = dict(func_dict)
    server = mongo_libs.create_instance(
        args.get_val("-c"), args.get_val("-d"), mongo_class.Server)
    state = server.connect()

    if state[0]:
        # Call functions - intersection of command line and function dictionary
        for item in set(args.get_args_keys()) & set(func_dict.keys()):
            status = func_dict[item](server, args)

            if not status[0]:
                print(f"Error:  {status[1]}")
                break

        mongo_libs.disconnect([server])

    else:
        print(f"Connection failure:  {state[1]}")


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains directories and their octal permissions
        file_perm_chk -> file check options with their perms in octal
        file_crt -> contains options which require files to be created
        func_dict -> dictionary list for the function calls or other options
        opt_arg_list -> contains optional arguments for the command line
        opt_con_req_dict -> contains options requiring one or more options
        opt_con_req_list -> contains the options that require other options
        opt_def_dict -> contains options with their default values
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains the options that are required for the program
        opt_val_list -> contains options which require values
        opt_valid_val -> contains a list of valid values for options
        opt_xor_dict -> contains dict with key that is xor with it's values

    Arguments:
        (input) argv -> Arguments from the command line

    """

    dir_perms_chk = {"-d": 5, "-n": 7}
    file_perm_chk = {"-o": 6}
    file_crt = ["-o"]
    func_dict = {
        "-C": defrag, "-D": dbcc, "-M": get_status, "-L": rotate,
        "-G": get_log}
    opt_con_req_dict = {"-t": ["-C", "-D"]}
    opt_con_req_list = {
        "-i": ["-m"], "-n": ["-L"], "-f": ["-D"], "-s": ["-e"], "-u": ["-e"],
        "-w": ["-o"], "-k": ["-r"]}
    opt_def_dict = {
        "-C": [], "-D": [], "-G": "global", "-i": "sysmon:mongo_db_status"}
    opt_multi_list = ["-C", "-D", "-t", "-e", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = [
        "-c", "-d", "-t", "-C", "-D", "-i", "-m", "-o", "-G", "-n", "-e", "-s",
        "-y", "-w"]
    opt_valid_val = {"-G": ["global", "rs", "startupWarnings"]}
    opt_xor_dict = {
        "-L": ["-C", "-M", "-D"], "-C": ["-D", "-M", "-L"],
        "-D": ["-C", "-M", "-L"], "-M": ["-C", "-D", "-L", "-G"], "-G": ["-M"]}

    # Process argument list from command line.
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, opt_def=opt_def_dict,
        multi_val=opt_multi_list)

    if args.arg_parse2(                                 # pylint:disable=R0916
       ) and not gen_libs.help_func(args, __version__, help_message)        \
       and args.arg_require(opt_req=opt_req_list)                           \
       and args.arg_valid_val(opt_valid_val=opt_valid_val)                  \
       and args.arg_xor_dict(opt_xor_val=opt_xor_dict)                      \
       and args.arg_cond_req_or(opt_con_or=opt_con_req_dict)                \
       and args.arg_cond_req(opt_con_req=opt_con_req_list)                  \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)                    \
       and args.arg_file_chk(file_perm_chk=file_perm_chk, file_crt=file_crt):

        try:
            prog_lock = gen_class.ProgramLock(
                sys.argv, args.get_val("-y", def_val=""))
            run_program(args, func_dict)
            del prog_lock

        except gen_class.SingleInstanceException:
            print(f'WARNING:  lock in place for mongo_db_admin with id of:'
                  f' {args.get_val("-y", def_val="")}')


if __name__ == "__main__":
    sys.exit(main())
