#!/bin/bash
# Unit test code coverage for SonarQube to cover the mongo_db_admin functions.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/dbcc.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/defrag.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/get_log.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/help_message.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/main.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/process_dbs_tbls.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/process_mail.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/process_request.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/repair_db.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/rotate.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/run_compact.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/run_dbcc.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/run_program.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/run_repair.py
coverage run -a --source=mongo_db_admin test/unit/mongo_db_admin/status.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

