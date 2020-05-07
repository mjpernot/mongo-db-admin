#!/usr/bin/python
# Classification (U)

"""Program:  run_repair.py

    Description:  Unit testing of run_repair in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/run_repair.py

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


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for mongo_class.DB class.

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
        self.db_results = {"ok": 1}

    def chg_db(self, dbn):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.DB.chg_db method.

        Arguments:
            (input) dbn -> Database name.

        """

        return True

    def db_cmd(self, cmd):

        """Method:  db_cmd

        Description:  Stub holder for mongo_class.DB.db_cmd method.

        Arguments:
            (input) cmd -> Database command.

        """

        return self.db_results


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_errors -> Test with errors detected.
        test_no_errors -> Test with no errors detected.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()
        self.db_name = "DatabaseName"

    def test_errors(self):

        """Function:  test_errors

        Description:  Test with errors detected.

        Arguments:

        """

        self.mongo.db_results = {"ok": 0}

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_repair(self.mongo,
                                                       self.db_name))

    def test_no_errors(self):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_repair(self.mongo,
                                                       self.db_name))


if __name__ == "__main__":
    unittest.main()
