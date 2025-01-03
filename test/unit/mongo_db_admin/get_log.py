# Classification (U)

"""Program:  get_log.py

    Description:  Unit testing of get_log in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/get_log.py

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
import mongo_db_admin                           # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mongo", "-d": "config", "-G": "rs"}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Server():                                         # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        adm_cmd

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None
        self.arg1 = None
        self.name = "ServerName"

    def adm_cmd(self, cmd, arg1):

        """Method:  adm_cmd

        Description:  Stub holder for mongo_class.Server.adm_cmd method.

        Arguments:

        """

        self.cmd = cmd
        self.arg1 = arg1

        return {"log": "value"}


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
                         "get_log: Error encountered: Connection Failure")

    @mock.patch("mongo_db_admin.data_out")
    def test_data_out_fail(self, mock_out):

        """Function:  test_data_out_fail

        Description:  Test with data_out failure.

        Arguments:

        """

        mock_out.return_value = self.status2

        self.assertEqual(
            mongo_db_admin.get_log(self.server, self.args), self.results2)

    @mock.patch("mongo_db_admin.data_out")
    def test_data_out_success(self, mock_out):

        """Function:  test_data_out_success

        Description:  Test with data_out successful.

        Arguments:

        """

        mock_out.return_value = self.status

        self.assertEqual(
            mongo_db_admin.get_log(self.server, self.args), self.results)


if __name__ == "__main__":
    unittest.main()
