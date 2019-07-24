#!/usr/bin/python
# Classification (U)

"""Program:  run_compact.py

    Description:  Unit testing of run_compact in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/run_compact.py

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

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.
        chg_db -> Stub holder for mongo_class.DB.chg_db method.
        get_tbl_list -> Stub holder for mongo_class.DB.get_tbl_list method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_name = "DatabaseName"
        self.tbl_list = []

    def chg_db(self, db):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.DB.chg_db method.

        Arguments:
            (input) db -> Database name.

        """

        return True

    def get_tbl_list(self, status):

        """Method:  get_tbl_list

        Description:  Stub holder for mongo_class.DB.get_tbl_list method.

        Arguments:
            (input) status -> Status of check.

        """

        return self.tbl_list


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_no_tbl_list -> Test with empty table list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()
        self.db_name = "DatabaseName"
        self.tbl_name = ["Table3", "Table4"]

    def test_tbl_list(self):

        """Function:  test_tbl_list

        Description:  Test with table list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_compact(self.mongo,
                                                        self.db_name))


if __name__ == "__main__":
    unittest.main()
