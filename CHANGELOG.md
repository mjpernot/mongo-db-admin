# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.0.1] - 2018-11-30
### Fixed
- main:  Corrected incorrect function name calls.
- run_compact:  Changed function parameter mutable argument default to immutable argument default.
- run_dbcc:  Changed function parameter mutable argument default to immutable argument default.
- process_request:  Changed function parameter mutable argument default to immutable argument default.

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
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
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
- Help_Message:  Replace docstring with printing the programs __doc__.
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
- Help_Message:  Updated documentation to reflect the changes in the Mongo configuration file format for the two types of connections.  Also included a new Known Bug entry.


## [1.8.0] - 2017-04-12
### Added
- Added the new function 'full' check to the database validation option.

### Changed
- DBCC:  Added named argment 'full' to function call.
- Process_Request:  Added **kwargs to a number of func_name function calls.  Also added **kwargs to the function argment list.
- Run_DBCC:  Added **kwargs to the function argment list.  Changed function name to validate_tbl and also added named argument 'scan' to function call.
- main:  Added -f option to opt_con_req_list variable.
- Help_Message:  Updated documentation.


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
- Help_Message:  Updated documentation.


## [1.5.0] - 2017-01-24
### Added
- Added error exception handling in several functions and also allowed multiple database and tables names to be passed to the program.

### Changed
- Help_Message:  Updated documentation.
- Process_Request:  Added connect() for the class.  Set default values for arguments.  Changed 'if' statement to deal with multiple values for databases and tables and use generators to build lists.
- Run_Compact:  Changed print to use format option.
- Run_DBCC:  Changed print to use format option.
- Run_Repair:  Changed print to use format option.
- Defrag:  Added error exception handling code.
- Run_Program:  Added error exception handling code.
- DBCC:  Added error exception handling code.
- Repair_DB:  Added error exception handling code.
- Status:  Added error exception handling code.
- Rotate:  Added error exception handling code.
- Get_Log:  Added error exception handling code.


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
- Help_Message:  Added new option to help message.


## [1.2.0] - 2016-04-26
### Added
- Added new option "-L" to roate the log file.
- Rotate function.

### Changed
- Help_Message:  Added new option to help message.
- main:  Added option "-L" to the func_dict variable.


## [1.1.0] - 2016-04-19
### Added
- Added new functionality to check the status of the database by checking on connection usage, memory usage, and uptime.
- Status function.

### Changed
- main:  Added options "-M", "-m", "-f", "-i", and "-o" options to a number of variables and added a number of new function call checks.
- Run_Program:  Processing for some of the new options and passing to the functions as named arguments.  Also setup a Mongo Rep Set instance.
- Help_Message:  Added new options to help message.


## [1.0.0] - 2016-03-09
- Initial creation.
