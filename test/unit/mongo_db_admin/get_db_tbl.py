# Classification (U)

"""Program:  get_db_tbl.py

    Description:  Unit testing of get_db_tbl in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/get_db_tbl.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_list = None
        self.tbl_list = None
        self.inc_sys = True

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
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
#        self.fetch_db2 = [{"Database": "db1"}, {"Database": "db2"}]
        self.fetch_dbs3 = ["systemdb"]
#        self.db_list = list()
        self.db_list2 = ["db1"]
        self.db_list3 = ["systemdb"]
#        self.db_list4 = ["systemdb", "db1"]
        self.db_list5 = ["db1", "db2"]
#        self.tbl_list = ["t2"]
        self.tbl_list2 = ["t1", "t2"]
#        self.tbl_dict = [{"TABLE_NAME": "t2"}]
#        self.tbl_dict2 = [{"TABLE_NAME": "t1"}, {"TABLE_NAME": "t2"}]
#        self.tbl_dict56 = [{"table_name": "t1"}, {"table_name": "t2"}]
        self.all_tbls = {"db1": ["t2"]}
        self.all_tbls2 = {"db1": ["t2"], "db2": ["t1"]}
        self.ign_dbs = ["systemdb"]
        self.results = {"db1": ["t2"]}
        self.results2 = {"db1": ["t2"], "db2": ["t1"]}
        self.results3 = dict()
        self.results4 = {"db1": ["t1", "t2"]}

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

        self.args.args_array["-t"] = self.tbl_list

        mock_fetch.return_value = self.tbl_dict2

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.args, self.db_list2, sys_dbs=self.sys_dbs),
            self.results)

    @mock.patch("mongo_db_admin.get_all_dbs_tbls")
    def test_with_system_db_only3(self, mock_all):

        """Function:  test_with_system_db_only3

        Description:  Test with system and user database list.

        Arguments:

        """

        mock_fetch.return_value = self.fetch_db3
        mock_all.return_value = self.all_tbls

        self.assertEqual(
            mongo_db_admin.get_db_tbl(
                self.server, self.args, self.db_list4, sys_dbs=self.sys_dbs),
            self.results)

    def test_with_system_db_only2(self):

        """Function:  test_with_system_db_only2

        Description:  Test with empty database list.

        Arguments:

        """

        mock_fetch.return_value = self.fetch_dbs3

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
                self.server, self.args, self.db_list), self.results2)

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
