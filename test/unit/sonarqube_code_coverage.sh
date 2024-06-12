#!/bin/bash
# Unit test code coverage for SonarQube to cover the mongo_db_admin functions.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/compact.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/dbcc.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/defrag.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/get_log.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/help_message.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/main.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/rotate.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/run_program.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/status.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/create_data_config.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/data_out.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/get_all_dbs_tbls.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/get_db_tbl.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/get_json_template.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

