#!/usr/bin/python
# Classification (U)

"""Program:  process_dbs_tbls.py

    Description:  Unit testing of process_dbs_tbls in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/process_dbs_tbls.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mongo_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def func_name(mongo, dbn, tbl_list=None, **kwargs):

    """Method:  func_name

    Description:  Stub holder for genertic function.

    Arguments:
        (input) mongo -> Mongo instance.
        (input) dbn -> Database name.
        (input) tbl_list -> Table name list.
        (input) kwargs:
            mail => Mail instance.

    """

    status = True
    mail = kwargs.get("mail", None)

    if mongo and dbn and tbl_list and mail:
        status = True

    return status


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for mongo_class.DB class.

    Methods:
        __init__
        chg_db
        get_tbl_list

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.dbn = None
        self.tbl_list = ["Table1", "Table2"]

    def chg_db(self, dbs):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.DB.chg_db method.

        Arguments:
            (input) dbn -> Database name.

        """

        self.dbn = dbs

        return True

    def get_tbl_list(self):

        """Method:  get_tbl_list

        Description:  Stub holder for mongo_class.DB.get_tbl_list method.

        Arguments:

        """

        return self.tbl_list


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_not_found_tbl
        test_not_found_db
        test_multiple_tbl_list
        test_multiple_db_list
        test_single_tbl_list
        test_single_db_list
        test_no_tbl_list
        test_no_db_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()
        self.func_name = func_name
        self.db_name = []
        self.db_name2 = ["DB1"]
        self.db_name3 = ["DB1", "DB2"]
        self.db_name4 = ["DB3"]
        self.db_list = ["DB1", "DB2"]
        self.tbl_name = []
        self.tbl_name2 = ["Table1"]
        self.tbl_name3 = ["Table1", "Table2"]
        self.tbl_name4 = ["Table3", "Table4"]
        self.tbl_list = ["Table1", "Table2"]

    def test_not_found_tbl(self):

        """Function:  test_not_found_tbl

        Description:  Test with table not found.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_dbs_tbls(
                self.mongo, self.func_name, self.db_name3, self.db_list,
                self.tbl_name4))

    def test_not_found_db(self):

        """Function:  test_not_found_db

        Description:  Test with database not found.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_dbs_tbls(
                self.mongo, self.func_name, self.db_name4, self.db_list,
                self.tbl_name2))

    def test_multiple_tbl_list(self):

        """Function:  test_multiple_tbl_list

        Description:  Test with multiple tables in list.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_dbs_tbls(
                self.mongo, self.func_name, self.db_name2, self.db_list,
                self.tbl_name3))

    def test_multiple_db_list(self):

        """Function:  test_multiple_db_list

        Description:  Test with multiple databases in list.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_dbs_tbls(
                self.mongo, self.func_name, self.db_name3, self.db_list,
                self.tbl_name2))

    def test_single_tbl_list(self):

        """Function:  test_single_tbl_list

        Description:  Test with single table in list.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_dbs_tbls(
                self.mongo, self.func_name, self.db_name2, self.db_list,
                self.tbl_name2))

    def test_single_db_list(self):

        """Function:  test_single_db_list

        Description:  Test with single database in list.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_dbs_tbls(
                self.mongo, self.func_name, self.db_name2, self.db_list,
                self.tbl_name2))

    def test_no_tbl_list(self):

        """Function:  test_no_tbl_list

        Description:  Test with no table in list.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_dbs_tbls(
                self.mongo, self.func_name, self.db_name2, self.db_list,
                self.tbl_name))

    def test_no_db_list(self):

        """Function:  test_no_db_list

        Description:  Test with no database in list.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_dbs_tbls(
                self.mongo, self.func_name, self.db_name, self.db_list,
                self.tbl_name2))


if __name__ == "__main__":
    unittest.main()

