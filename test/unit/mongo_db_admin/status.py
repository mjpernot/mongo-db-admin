# Classification (U)

"""Program:  status.py

    Description:  Unit testing of status in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/status.py

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


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mongo", "-d": "config"}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        upd_srv_stat

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"
        self.cur_mem = 1000
        self.max_mem = 10000
        self.prct_mem = 10
        self.days_up = 1
        self.cur_conn = 9
        self.max_conn = 100
        self.prct_conn = 11

    def upd_srv_stat(self):

        """Method:  upd_srv_stat

        Description:  Stub holder for mongo_class.Server.upd_srv_stat method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_data_out_fail
        test_data_out_success

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.status = (True, None)
        self.status2 = (False, "Connection Failure")
        self.results = (True, None)
        self.results2 = (False,
                         "defrag: Error encountered: Connection Failure")

    @mock.patch("mongo_db_admin.data_out")
    def test_data_out_fail(self, mock_out):

        """Function:  test_data_out_fail

        Description:  Test with data_out failure.

        Arguments:

        """

        mock_out.return_value = self.status2

        self.assertEqual(
            mongo_db_admin.status(self.server, self.args), self.results2)

    @mock.patch("mongo_db_admin.data_out")
    def test_data_out_success(self, mock_out):

        """Function:  test_data_out_success

        Description:  Test with data_out successful.

        Arguments:

        """

        mock_out.return_value = self.status

        self.assertEqual(
            mongo_db_admin.status(self.server, self.args), self.results)


if __name__ == "__main__":
    unittest.main()
