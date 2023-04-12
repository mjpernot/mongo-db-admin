# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.4.3] - 2022-11-30
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded mongo-lib to v4.2.2
 
### Fixed:
- process_request: Added SSL entries to the mongo_class instance calls.

### Changed
- process_request: Made auth_mech a required parameter, cannot be passed as an empty argument anymore.
- Converted imports to use Python 2.7 or Python 3.


## [2.4.2] - 2022-07-18
- Removed the -R option as this option is not available in Mongo 4.2.

### Fixed
- run_compact: System databases are non-compactable and are skipped.
- status: Moved json.dumps call to after Mongo database insert as json.dumps was converting "none" to "null".

### Added
- compact: Runs the compact command and checks the status return.

### Changed
- status: Removed checks on data type for Mongo insertion and refactored function.
- process_request: Removed "use_arg" and "use_uri" from mongo_class.DB instance call.

### Removed
- run_repair, repair_db: The "repairDatabase" command is longer available in Mongo 4.2.


## [2.4.1] - 2022-06-28
- Upgrade mongo-libs to v4.2.1
- Upgrade python-lib to v2.9.2

### Changed
- config/mongo.py.TEMPLATE: Removed old entries.
- Documentation updates.


## [2.4.0] - 2021-09-09
- Updated to work in Mongo 4.2.14 environment.
- Updated to work in a SSL environment.
- Added ability to override the default mail command and use mailx.

### Added
- process_dbs_tbls:  Process a list of databases and tables.
- process_mail:  Add data to mail instance and send mail.

### Changed
- process_request:  Added auth_mech to mongo_class instance call.
- main:  Add -u option to the conditional required list.
- config/mongo.py.TEMPLATE:  Added SSL connection entries.
- process_request:  Replaced process databases and tables with call to process_dbs_tbls and combined a number of if and else statements into a single statement.
- status:  Replaced email section with call to process_mail.
- run_compact:  Combined if and else into a single statement.
- Documentation updates.


## [2.3.2] - 2020-12-29
- Verified to work with pymongo v3.8.0.
- Updated to be used in FIPS 140-2 environment.

### Fixed
- process_request:  When using the -t option, do not process a database if no tables are present.
- get_log:  Added Server and AsOf to the JSON document.

### Changed
- run_compact, repair_db, defrag, dbcc, process_request, status, run_program:  Capture and process connection status.
- process_request, run_compact, run_program:  Replaced cmds_gen.disconnect with mongo_libs.disconnect.
- Upgrade to use mongo-libs v4.1.0 library.
- process_request:  Updated Mongo class instance to reflect changes in config file.
- config/mongo.py.TEMPLATE:  Added authentication mechanism entries to config file.
- Documentation updates.

### Removed
- Removed cmds_gen library module, no longer required. 


## [2.3.1] - 2020-05-04
### Added
- Added -p option to allow compression of Mongo log with Log Rotate option.
- Added -y option to allow a flavor ID for the program lock.

### Fixed
- status:  Write to file in correct format.

### Changed
- run_program:  Removed sys.exit() call.
- status:  Refactored the email code section to reduce complexity.
- config/mongo.py.TEMPLATE:  Set the replica set variables to None.
- status:  Changed JSON key values to PascalCase.
- rotate:  Added option compression call when rotating log files to -n option directory.
- main:  Added program lock functionality to program.


## [2.3.0] - 2020-04-16
### Added
- Added -g option to Flatten the JSON data structure to file and standard out.
- Added -a option to allow for append of data to an existing output file.

### Fixed
- run_dbcc, rotate:  Changed "status" to "status_flag" due to naming conflict.
- main:  Fixed handling command line arguments from SonarQube scan finding.

### Changed
- status, get_log: Added file mode option to writing data to a file.  Default is write.
- status, get_log:  Added flattening of JSON structure to standard out and to file.
- Removed unused libraries getpass and socket.
- Documentation updates.


## [2.2.0] - 2019-10-16
### Fixed
- status:  Allow printing to standard out for the -M and -j argument combination.
- run_dbcc:  Fixed validation of views in Mongo.

### Changed
- defrag:  Changed error message to warning message.
- status:  Refactored entire function to be more streamline.
- run_program:  Replaced setup_mail() call with gen_class.setup_mail() call.
- process_request:  Changed a number of arguments from positional to keyword arguments.

### Removed
- setup_mail:  Replaced by gen_class.setup_mail function.

### Added
- Added -z option to program to allow standard out suppression.


## [2.1.0] - 2019-07-24
### Fixed
- Fixed mutable list/dictionary argument issues in a number of functions.

### Changed
- status:  Added capability to mail out JSON formatted data.
- run_program:  Added setup of mail instance and passing mail instance to functions.
- main:  Added '-e' and '-s' options to allow for email capability for some options.
- status:  Replaced mongo_libs.json_prt_ins_2_db call with own internal code.
- status:  Converted JSON output to camelCase.
- main:  Refactored 'if' statement to streamline the checks.
- Updated variables names to standard convention.
- run_compact, run_repair:  Added \*\*kwargs to argument list.

### Added
- setup_mail:  Initialize a mail instance.


## [2.0.1] - 2018-11-30
### Fixed
- main:  Corrected incorrect function name calls.
- run_compact, run_dbcc, process_request:  Changed function parameter mutable argument default to immutable argument default.

### Changed
- main:  Removed non-used argument in run_program call.


## [2.0.0] - 2018-04-30
Breaking Change

### Changed
- rotate:  Change "mongo_libs.Fetch_Cmd_Line" with "mongo_class.fetch_cmd_line" call.
- defrag:  Change "mongo_libs.Fetch_isMaster" with "mongo_class.fetch_ismaster" call.
- Changed "mongo_libs" calls to new naming schema.
- Changed "cmds_gen" calls to new naming schema.
- rotate:  Refactor code to use "gen_libs.chk_crt_dir" call.
- get_log:  Replaced "gen_libs.Write_File" to "gen_libs.write_file2" call.
- get_log:  Replaced "gen_libs.Close_File" with system close call.
- get_log:  Replaced "gen_libs.Open_File" with system open call.
- Changed "gen_libs" and "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [1.12.0] - 2018-04-26
Breaking Change

### Changed
- Changed "cmds_mongo" to "mongo_libs" module reference.
- Changed "svr_mongo" to "mongo_class" module reference.

### Added
- Added single-source version control.


## [1.11.1] - 2017-08-28
### Fixed
- Status -> Standard out is not writing to a file.
- Status:  Both JSON and standard out will use the same dictionary data structure.  Replace "print"s with calls to functions and "if" will either write to a file or print to std out.
- Get_Log:  Add code to open and write to a file or write to standard out.


## [1.11.0] - 2017-08-21
### Changed
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.
- Change single quotes to double quotes.
- Convert program to use local libraries from ./lib directory.
- Run_Program:  Change REP_SET to Rep_Cfg to be standardized.


## [1.10.0] - 2017-05-12
### Fixed
- Mongo 3.4:  Prevents compact operations on some capped system collections.  Per Mongo docs, all capped collections do not require compact operations to be run against them.
- Run_Compact:  Added check that if collection is capped, then skip it.


## [1.9.0] - 2017-04-17
### Added
- Added the ability for the -i option to connect to either a single Mongo database server or to a Mongo replica set. This will require svr_mongo V1.10 or better and cmds_mongo V1.5 or better.  Also the Mongo database configuration file will need to be modified to allow a connection to a Mongo replica set.

### Changed
- Update documentation.


## [1.8.0] - 2017-04-12
### Added
- Added the new function 'full' check to the database validation option.

### Changed
- DBCC:  Added named argment 'full' to function call.
- Process_Request:  Added \*\*kwargs to a number of func_name function calls.  Also added \*\*kwargs to the function argment list.
- Run_DBCC:  Added \*\*kwargs to the function argment list.  Changed function name to validate_tbl and also added named argument 'scan' to function call.
- main:  Added -f option to opt_con_req_list variable.
- Updated documentation.


## [1.7.0] - 2017-04-11
### Changed
- Replaced the -f option with -j and -l options.  Will assume standard out for everything unless -j or -l option is used.
- main:  Added -j and -l options and remove -f option.  Also added additional check function - Arg_Cond_Req_Or.
- Run_Program:  Removed the frmt variable as checking the output format will now be done in individual functions.
- Get_Log:  Replaced checking the named "form" argument with checking the args_array directly for the -j and -l options and assume "standard out" for everything else.  Removed err_flag and err_msg variables.
- Status:  Replaced checking the named "form" argument with checking the args_array directly for the -j option or else assume "standard out".  Also refactored the code from three "if"s into a single "if" statement.  Removed err_flag and err_msg variables.


## [1.6.0] - 2017-04-07
### Added
- Added new functionality to allow the mongo database error log to be moved to another directory when the Log Rotate option is used.

### Changed
- Rotate:  Rewrote the entire function to handle moving the old Mongo log to another directory with the -n option.
- Updated documentation.


## [1.5.0] - 2017-01-24
### Added
- Added error exception handling in several functions and also allowed multiple database and tables names to be passed to the program.

### Changed
- Process_Request:  Added connect() for the class.  Set default values for arguments.  Changed 'if' statement to deal with multiple values for databases and tables and use generators to build lists.
- Run_Compact, Run_DBCC, Run_Repair:  Changed print to use format option.
- Defrag, Run_Program, DBCC, Repair_DB, Status, Rotate, Get_Log:  Added error exception handling code.
- Updated documentation.


## [1.4.0] - 2016-05-16
### Fixed
- Process_Request:  Changed auth and conf_file parameters to the SERVER class settings.


## [1.3.0] - 2016-04-28
### Added
- Added new option "-G" option which will retrieve the mongo error log that currently resides in the mongo memory.  Includes a format options and types of logs to be retrieved.
- Get_Log function.

### Changed
- main:  Added option "-G" to a number of variables, added new variable: opt_valid_val, and added Arg_Valid_Val function call.
- Status:  Added additional check due to new format options.
- Updated documentation.


## [1.2.0] - 2016-04-26
### Added
- Added new option "-L" to roate the log file.
- Rotate function.

### Changed
- main:  Added option "-L" to the func_dict variable.
- Updated documentation.


## [1.1.0] - 2016-04-19
### Added
- Added new functionality to check the status of the database by checking on connection usage, memory usage, and uptime.
- Status function.

### Changed
- main:  Added options "-M", "-m", "-f", "-i", and "-o" options to a number of variables and added a number of new function call checks.
- Run_Program:  Processing for some of the new options and passing to the functions as named arguments.  Also setup a Mongo Rep Set instance.
- Updated documentation.


## [1.0.0] - 2016-03-09
- Initial creation.

