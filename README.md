# Python project for administration of a Mongo database.
# Classification (U)

# Description:
  This is used to adminstrate a Mongo database, to include repairing, defragmentation, and validatine tables.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features
  * Repair a Mongo database.
  * Validate one or more tables/collections in a Mongo database.
  * Defragmentation of a database or table in a Mongo database server.
  * Display current status of a Mongo database.
  * Check for errors in the Mongo log that is stored in Mongo memory cache.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - mongo_lib/mongo_class
    - mongo_lib/mongo_libs


# Installation:

Install this project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-db-admin.git
```

Install/upgrade system modules.

```
cd mongo-db-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create Mongodb configuration file.

```
cd config
cp mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```


# Program Descriptions:
### Program: mongo-db-admin.py
##### Description: Administration program for a Mongo database.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}mongo-db-admin/mongo-db-admin.py -h
```


# Help Message:
  Below is the help message for the program.  Recommend running the -h option on the command line to see the latest help message.

    Program:  mongo-db-admin.py
    Description:  A Mongo Database Administration program that can run a number
        of different administration functions such as repairing a database,
        compacting/defraging tables or entire database, or validating
        tables in a database.  Can return the database's status to
        include uptime, connection usage, and memory use and can also
        retrieve the Mongo error log that currently resides in memory.

    Usage:
        mongo_db_admin.py -c file -d path -L [-n dir_path] |
            {-R [db_name [db_name ...]]} | {-C [db_name
            [db_name ...]] [-t table_name [table_name ...]]} |
            {-D [ db_name [ db_name ... ] ] [ -t table_name
            [table_name ...]]} | [-f] {-M {-j | -i db_name:table_name |
            -m file | -o dir_path/file } } |
            {-G { global | rs | startupWarnings} | {-j | -l |
            -o dir_path/file}} [-v | -h]

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


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mongo-db-admin.py program.

### Installation:

Install this project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-db-admin.git
```

Install/upgrade system modules.

```
cd mongo-db-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for mongo-db-admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-db-admin
```

### Unit:  help_message
```
test/unit/mongo_db_admin/help_message.py
```

### Unit:  
```
test/unit/mongo_db_admin/
```

### Unit:  
```
test/unit/mongo_db_admin/
```

### Unit:  run_program
```
test/unit/mongo_db_admin/run_program.py
```

### Unit:  main
```
test/unit/mongo_db_admin/main.py
```

### All unit testing
```
test/unit/mongo_db_admin/unit_test_run.sh
```

### Code coverage program
```
test/unit/mongo_db_admin/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the mongo-db-admin.py program.

### Installation:

Install this project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-db-admin.git
```

Install/upgrade system modules.

```
cd mongo-db-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.

```
cd test/integration/mongo_db_admin/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Integration test runs for mongo-db-admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-db-admin
```


### Integration:  
```
test/integration/mongo_db_admin/
```

### All integration testing
```
test/integration/mongo_db_admin/integration_test_run.sh
```

### Code coverage program
```
test/integration/mongo_db_admin/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the mongo-db-admin.py program.

### Installation:

Install this project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-db-admin.git
```

Install/upgrade system modules.

```
cd mongo-db-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.

```
cd test/blackbox/mongo_db_admin/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Blackbox test run for mongo-db-admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-db-admin
```


### Blackbox:  
```
test/blackbox/mongo_db_admin/blackbox_test.sh
```

