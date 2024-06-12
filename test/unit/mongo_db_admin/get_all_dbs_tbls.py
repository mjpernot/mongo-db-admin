# Classification (U)

"""Program:  get_all_dbs_tbls.py

    Description:  Unit testing of get_all_dbs_tbls in mongo_db_admin.py.

    Usage:
        python test/unit/mongo_db_admin/get_all_dbs_tbls.py
        python3 test/unit/mongo_db_admin/get_all_dbs_tbls.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_admin
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__
        get_tbl_list
        chg_db

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.inc_sys = False
        self.tbl_list = list()
        self.dbs = None

    def get_tbl_list(self, inc_sys):

        """Method:  get_tbl_list

        Description:  Return list of tables.

        Arguments:

        """

        self.inc_sys = inc_sys

        return self.tbl_list

    def chg_db(self, dbs):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.Server.chg_db method.

        Arguments:

        """

        self.dbs = dbs


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ignore_db_tbl2
        test_ignore_db_tbl
        test_multiple_dbs
        test_one_db
        test_no_db

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.db_list = ["db1"]
        self.db_list2 = ["db1", "db2"]
        self.db_list3 = list()
        self.tbl_list = ["t2"]
        self.tbl_list2 = ["t1", "t2"]
        self.ign_db_tbl = {"db1": ["t1"]}
        self.ign_db_tbl2 = {"db1": ["t1"], "db2": ["t2"]}
        self.results = {"db1": ["t2"]}
        self.results2 = {"db1": ["t1", "t2"], "db2": ["t1", "t2"]}
        self.results3 = dict()
        self.results4 = {"db1": ["t2"], "db2": ["t1"]}

    def test_ignore_db_tbl2(self):

        """Function:  test_ignore_db_tbl2

        Description:  Test with ignoring databases and tables.

        Arguments:

        """

        self.server.tbl_list = self.tbl_list2

        self.assertEqual(
            mongo_db_admin.get_all_dbs_tbls(
                self.server, self.db_list2, ign_db_tbl=self.ign_db_tbl2),
            self.results4)

    def test_ignore_db_tbl(self):

        """Function:  test_ignore_db_tbl

        Description:  Test with ignoring databases and tables.

        Arguments:

        """

        self.server.tbl_list = self.tbl_list2

        self.assertEqual(
            mongo_db_admin.get_all_dbs_tbls(
                self.server, self.db_list, ign_db_tbl=self.ign_db_tbl),
            self.results)

    def test_multiple_dbs(self):

        """Function:  test_multiple_dbs

        Description:  Test with multiple databases.

        Arguments:

        """

        self.server.tbl_list = self.tbl_list2

        self.assertEqual(
            mongo_db_admin.get_all_dbs_tbls(
                self.server, self.db_list2), self.results2)

    def test_one_db(self):

        """Function:  test_one_db

        Description:  Test with one database.

        Arguments:

        """

        self.server.tbl_list = self.tbl_list

        self.assertEqual(
            mongo_db_admin.get_all_dbs_tbls(
                self.server, self.db_list), self.results)

    def test_no_db(self):

        """Function:  test_no_db

        Description:  Test with no database list passed.

        Arguments:

        """

        self.assertEqual(
            mongo_db_admin.get_all_dbs_tbls(
                self.server, self.db_list3), self.results3)


if __name__ == "__main__":
    unittest.main()
