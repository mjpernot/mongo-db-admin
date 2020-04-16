# Python project for administration of a Mongo database.
# Classification (U)

# Description:
  This is used to adminstrate a Mongo database, to include repairing, defragmentation, and validatine tables.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


# Features
  * Repair a Mongo database.
  * Validate one or more tables/collections in a Mongo database.
  * Defragmentation of a database or table in a Mongo database server.
  * Display current status of a Mongo database.
  * Check for errors in the Mongo log that is stored in Mongo memory cache.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
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


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}mongo-db-admin/mongo-db-admin.py -h
```


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


# Testing:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-db-admin
test/unit/mongo_db_admin/unit_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/mongo-db-admin
test/unit/mongo_db_admin/code_coverage.sh
```

