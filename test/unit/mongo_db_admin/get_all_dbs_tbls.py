# Classification (U)

"""Program:  get_all_dbs_tbls.py

    Description:  Unit testing of get_all_dbs_tbls in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/get_all_dbs_tbls.py

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

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_multiple_dbs
        test_one_db

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.dict_key = "TABLE_NAME"
        self.db_list = ["db1"]
        self.db_list2 = ["db1", "db2"]
        self.tbl_dict = [{"TABLE_NAME": "t2"}]
        self.tbl_dict2 = [{"TABLE_NAME": "t1"}, {"TABLE_NAME": "t2"}]
        self.tbl_list = ["t2"]
        self.tbl_list2 = ["t1", "t2"]
        self.results = {"db1": ["t2"]}
        self.results2 = {"db1": ["t2"], "db2": ["t1", "t2"]}

    @mock.patch("mongo_db_admin.mysql_libs.fetch_tbl_dict")
    def test_multiple_dbs(self, mock_fetch):

        """Function:  test_multiple_dbs

        Description:  Test with multiple databases.

        Arguments:

        """

        mock_fetch.side_effect = [self.tbl_dict, self.tbl_dict2]

        self.assertEqual(
            mongo_db_admin.get_all_dbs_tbls(
                self.server, self.db_list2, self.dict_key), self.results2)

    @mock.patch("mongo_db_admin.mysql_libs.fetch_tbl_dict")
    def test_one_db(self, mock_fetch):

        """Function:  test_one_db

        Description:  Test with one database.

        Arguments:

        """

        mock_fetch.return_value = self.tbl_dict

        self.assertEqual(
            mongo_db_admin.get_all_dbs_tbls(
                self.server, self.db_list, self.dict_key), self.results)


if __name__ == "__main__":
    unittest.main()
