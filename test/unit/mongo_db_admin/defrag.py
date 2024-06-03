# Classification (U)

"""Program:  defrag.py

    Description:  Unit testing of defrag in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/defrag.py

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


def run_compact():

    """Method:  run_compact

    Description:  Stub holder for run_compact function.

    Arguments:

    """

    return True


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
        test_errors
        test_is_master
        test_no_errors

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args.args_array = {"-C": "Optionsetting", "-t": "option"}

    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    @mock.patch("mongo_db_admin.process_request")
    def test_errors(self, mock_process, mock_fetch):

        """Function:  test_errors

        Description:  Test with errors returned.

        Arguments:

        """

        mock_process.return_value = (True, "Error Message")
        mock_fetch.return_value = {"ismaster": False}

        self.assertEqual(
            mongo_db_admin.defrag(
                self.server, self.args), (True, "Error Message"))

    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    def test_is_master(self, mock_fetch):

        """Function:  test_is_master

        Description:  Test with database being the master.

        Arguments:

        """

        mock_fetch.return_value = {"ismaster": True, "setName": True}
        err_msg = "Warning: Cannot defrag - database is Primary in ReplicaSet."

        self.assertEqual(
            mongo_db_admin.defrag(self.server, self.args), (True, err_msg))

    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    @mock.patch("mongo_db_admin.process_request")
    def test_no_errors(self, mock_process, mock_fetch):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        mock_process.return_value = (False, None)
        mock_fetch.return_value = {"ismaster": False}

        self.assertEqual(
            mongo_db_admin.defrag(self.server, self.args), (False, None))


if __name__ == "__main__":
    unittest.main()
