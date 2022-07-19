#!/bin/bash
# Unit testing program for the mongo_db_admin.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
test/unit/mongo_db_admin/dbcc.py
test/unit/mongo_db_admin/defrag.py
test/unit/mongo_db_admin/get_log.py
test/unit/mongo_db_admin/help_message.py
test/unit/mongo_db_admin/main.py
test/unit/mongo_db_admin/process_dbs_tbls.py
test/unit/mongo_db_admin/process_mail.py
test/unit/mongo_db_admin/process_request.py
test/unit/mongo_db_admin/rotate.py
test/unit/mongo_db_admin/run_compact.py
test/unit/mongo_db_admin/run_dbcc.py
test/unit/mongo_db_admin/run_program.py
test/unit/mongo_db_admin/status.py
