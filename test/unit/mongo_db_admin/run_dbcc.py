#!/usr/bin/python
# Classification (U)

"""Program:  run_dbcc.py

    Description:  Unit testing of run_dbcc in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/run_dbcc.py

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
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for mongo_class.DB class.

    Methods:
        __init__ -> Class initialization.
        validate_tbl -> Stub holder for mongo_class.DB.validate_tbl method.
        chg_db -> Stub holder for mongo_class.DB.chg_db method.
        get_tbl_list -> Stub holder for mongo_class.DB.get_tbl_list method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_name = "DatabaseName"
        self.type = True

    def validate_tbl(self, tbl, scan):

        """Method:  validate_tbl

        Description:  Stub holder for mongo_class.DB.validate_tbl method.

        Arguments:
            (input) tbl -> Table name.
            (input) scan -> True|False - Full scan.

        """

        if self.type:
            return True, {"valid": False, "errors": "Error Message"}

        else:
            return False, "Cannot validate view"

    def chg_db(self, db):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.DB.chg_db method.

        Arguments:
            (input) db -> Database name.

        """

        return True

    def get_tbl_list(self):

        """Method:  get_tbl_list

        Description:  Stub holder for mongo_class.DB.get_tbl_list method.

        Arguments:

        """

        return ["Table1", "Table2"]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_tbl_list -> Test with table list.
        test_default -> Test with default arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()
        self.db_name = "DatabaseName"
        self.tbl_name = ["Table3", "Table4"]

    def test_validate_view(self):

        """Function:  test_validate_view

        Description:  Test with trying to validate a view.

        Arguments:

        """

        self.mongo.type = False

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_dbcc(self.mongo, self.db_name,
                                                     self.tbl_name))

    def test_tbl_list(self):

        """Function:  test_tbl_list

        Description:  Test with table list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_dbcc(self.mongo, self.db_name,
                                                     self.tbl_name))

    def test_default(self):

        """Function:  test_default

        Description:  Test with default arguments.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_dbcc(self.mongo, self.db_name))


if __name__ == "__main__":
    unittest.main()
