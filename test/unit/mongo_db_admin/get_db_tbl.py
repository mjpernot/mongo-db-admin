# Classification (U)

"""Program:  get_db_tbl.py

    Description:  Unit testing of get_db_tbl in mongo_db_admin.py.

    Usage:
        python test/unit/mongo_db_admin/get_db_tbl.py
        python3 test/unit/mongo_db_admin/get_db_tbl.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import mongo_db_admin                           # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        fetch_dbs
        get_tbl_list
        chg_db

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_list = []
        self.tbl_list = []
        self.inc_sys = True
        self.dbs = None

    def fetch_dbs(self):

        """Method:  fetch_dbs

        Description:  Return list of databases.

        Arguments:

        """

        return self.db_list

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
        test_with_ign_db_tbls
        test_with_ign_db_tbl
        test_with_db_tbl2
        test_with_db_tbl
        test_with_system_db_only3
        test_with_system_db_only2
        test_with_system_db_only
        test_with_empty_db_list
        test_with_multiple_dbs
        test_with_single_db

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

        self.fetch_dbs = ["db1"]
        self.fetch_dbs3 = ["systemdb"]
        self.db_list = []
        self.db_list2 = ["db1"]
        self.db_list3 = ["systemdb"]
        self.db_list4 = ["systemdb", "db1"]
        self.db_list5 = ["db1", "db2"]
        self.tbl_list = ["t2"]
        self.tbl_list2 = ["t1", "t2"]
        self.tbl_list3 = ["t1", "t2", "t3"]
        self.tbl_list4 = ["t1", "t2", "t3", "t4"]
        self.all_tbls = {"db1": ["t2"]}
        self.all_tbls2 = {"db1": ["t2"], "db2": ["t1"]}
        self.all_tbls3 = {"db1": ["t2", "t1"]}
        self.all_tbls4 = {"db1": ["t2", "t1", "t3"]}
        self.ign_dbs = ["systemdb"]
        self.ign_db_tbl = {"db1": ["t1"]}
        self.ign_db_tbl2 = {"db1": ["t1", "t2"]}
        self.results = {"db1": ["t2"]}
        self.results2 = {"db1": ["t2"], "db2": ["t1"]}
        self.results3 = {}
        self.results4 = {"db1": ["t1", "t2"]}
        self.results5 = {"db1": ["t3"]}

    def test_with_ign_db_tbls(self):

        """Function:  test_with_ign_db_tbls

        Description:  Test with ignore multiple tables in a database.

        Arguments:

        """

        self.server.tbl_list = self.tbl_list4

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.db_list2, tbls=self.tbl_list3,
                ign_db_tbl=self.ign_db_tbl2), self.results5)

    def test_with_ign_db_tbl(self):

        """Function:  test_with_ign_db_tbl

        Description:  Test with ignore single table in a database.

        Arguments:

        """

        self.server.tbl_list = self.tbl_list

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.db_list2, tbls=self.tbl_list2,
                ign_db_tbl=self.ign_db_tbl), self.results)

    def test_with_db_tbl2(self):

        """Function:  test_with_db_tbl2

        Description:  Test with database and tables.

        Arguments:

        """

        self.server.tbl_list = self.tbl_list2

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.db_list2, ign_dbs=self.ign_dbs),
            self.results4)

    def test_with_db_tbl(self):

        """Function:  test_with_db_tbl

        Description:  Test with database and table.

        Arguments:

        """

        self.server.tbl_list = self.tbl_list

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.db_list2, tbls=self.tbl_list,
                ign_dbs=self.ign_dbs), self.results)

    @mock.patch("mongo_db_admin.get_all_dbs_tbls")
    def test_with_system_db_only3(self, mock_all):

        """Function:  test_with_system_db_only3

        Description:  Test with system and user database list.

        Arguments:

        """

        mock_all.return_value = self.all_tbls

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.db_list4, ign_dbs=self.ign_dbs),
            self.results)

    def test_with_system_db_only2(self):

        """Function:  test_with_system_db_only2

        Description:  Test with empty database list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_admin.get_db_tbl(
                    self.server, self.db_list, ign_dbs=self.ign_dbs),
                self.results3)

    def test_with_system_db_only(self):

        """Function:  test_with_system_db_only

        Description:  Test with system only database passed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_admin.get_db_tbl(
                    self.server, self.db_list3, ign_dbs=self.ign_dbs),
                self.results3)

    @mock.patch("mongo_db_admin.get_all_dbs_tbls")
    def test_with_empty_db_list(self, mock_all):

        """Function:  test_with_empty_db_list

        Description:  Test with empty database list.

        Arguments:

        """

        self.server.db_list = self.fetch_dbs

        mock_all.return_value = self.all_tbls2

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.db_list), self.results2)

    @mock.patch("mongo_db_admin.get_all_dbs_tbls")
    def test_with_multiple_dbs(self, mock_all):

        """Function:  test_with_multiple_dbs

        Description:  Test with multiple databases.

        Arguments:

        """

        mock_all.return_value = self.all_tbls2

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.db_list5), self.results2)

    @mock.patch("mongo_db_admin.get_all_dbs_tbls")
    def test_with_single_db(self, mock_all):

        """Function:  test_with_single_db

        Description:  Test with single database.

        Arguments:

        """

        mock_all.return_value = self.all_tbls

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.db_list2), self.results)


if __name__ == "__main__":
    unittest.main()
