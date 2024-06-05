# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/run_program.py

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


def dbcc(server, args_array):

    """Method:  dbcc

    Description:  Stub holder for dbcc function.

    Arguments:

    """

    flag = True
    errmsg = "ErrorMessage"

    if server and args_array:
        flag = True
        errmsg = "ErrorMessage"

    return flag, errmsg


def defrag(server, args_array):

    """Method:  defrag

    Description:  Stub holder for defrag function.

    Arguments:

    """

    flag = False
    errmsg = None

    if server and args_array:
        flag = False
        errmsg = None

    return flag, errmsg


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val
        get_args_keys

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

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.status = True
        self.errmsg = None

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Server.connect method.

        Arguments:

        """

        return self.status, self.errmsg


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_connection_failure
        test_connection_successful
        test_func_failure

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {"-c": True, "-d": True, "-C": True}
        self.args2.args_array = {
            "-c": True, "-d": True, "-C": True, "-m": True}
        self.args3.args_array = {
            "-c": True, "-d": True, "-C": True, "-m": True, "-e": "ToEmail",
            "-s": "SubjectLine"}
        self.func_names = {"-C": defrag}
        self.func_names2 = {"-C": dbcc}

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_connection_failure(self, mock_mongo):

        """Function:  test_connection_failure

        Description:  Test with failed connection.

        Arguments:

        """

        self.server.status = False
        self.server.errmsg = "Connection failure"
        mock_mongo.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_db_admin.run_program(self.args, self.func_names))

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_connection_successful(self, mock_mongo):

        """Function:  test_connection_successful

        Description:  Test with successful connection.

        Arguments:

        """

        mock_mongo.return_value = self.server

        self.assertFalse(
            mongo_db_admin.run_program(self.args, self.func_names))

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_func_failure(self, mock_mongo):

        """Function:  test_func_failure

        Description:  Test with function returning error message.

        Arguments:

        """

        mock_mongo.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_db_admin.run_program(self.args2, self.func_names2))


if __name__ == "__main__":
    unittest.main()
