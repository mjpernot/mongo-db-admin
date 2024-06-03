# Classification (U)

"""Program:  dbcc.py

    Description:  Unit testing of dbcc in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/dbcc.py

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


def run_dbcc():

    """Method:  run_dbcc

    Description:  Stub holder for run_dbcc function.

    Arguments:

    """

    return True


class ArgParser(object):

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

        self.args_array = {"-c": "mongo", "-d": "config"}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False

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
        test_dbcc2
        test_dbcc

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args.args_array = {"-D": "Optionsetting", "-t": "option"}

    @mock.patch("mongo_db_admin.process_request")
    def test_dbcc2(self, mock_process):

        """Function:  test_dbcc2

        Description:  Test dbcc function.

        Arguments:

        """

        mock_process.return_value = (True, "Error Message")

        self.assertEqual(
            mongo_db_admin.dbcc(
                self.server, self.args), (True, "Error Message"))

    @mock.patch("mongo_db_admin.process_request")
    def test_dbcc(self, mock_process):

        """Function:  test_dbcc

        Description:  Test dbcc function.

        Arguments:

        """

        mock_process.return_value = (False, None)

        self.assertEqual(
            mongo_db_admin.dbcc(self.server, self.args), (False, None))


if __name__ == "__main__":
    unittest.main()
