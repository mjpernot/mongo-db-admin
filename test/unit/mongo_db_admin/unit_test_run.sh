#!/bin/bash
# Unit testing program for the mongo_db_admin.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
/usr/bin/python test/unit/mongo_db_admin/compact.py
/usr/bin/python test/unit/mongo_db_admin/dbcc.py
/usr/bin/python test/unit/mongo_db_admin/defrag.py
/usr/bin/python test/unit/mongo_db_admin/get_log.py
/usr/bin/python test/unit/mongo_db_admin/help_message.py
/usr/bin/python test/unit/mongo_db_admin/main.py
/usr/bin/python test/unit/mongo_db_admin/process_dbs_tbls.py
/usr/bin/python test/unit/mongo_db_admin/process_mail.py
/usr/bin/python test/unit/mongo_db_admin/process_request.py
/usr/bin/python test/unit/mongo_db_admin/rotate.py
/usr/bin/python test/unit/mongo_db_admin/run_compact.py
/usr/bin/python test/unit/mongo_db_admin/run_dbcc.py
/usr/bin/python test/unit/mongo_db_admin/run_program.py
/usr/bin/python test/unit/mongo_db_admin/status.py
/usr/bin/python test/unit/mongo_db_admin/create_data_config.py
/usr/bin/python test/unit/mongo_db_admin/data_out.py
/usr/bin/python test/unit/mongo_db_admin/get_all_dbs_tbls.py
/usr/bin/python test/unit/mongo_db_admin/get_db_tbl.py
/usr/bin/python test/unit/mongo_db_admin/get_json_template.py
