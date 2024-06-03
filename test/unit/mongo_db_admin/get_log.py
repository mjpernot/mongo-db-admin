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
import mongo_db_admin
import version

__version__ = version.__version__


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
            (input) cmd -> Command.
            (input) arg1 -> Argument one.

        """

        self.cmd = cmd
        self.arg1 = arg1

        return {"log": "value"}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_to_json_flatten
        test_to_json
        test_to_list
        test_append_to_file
        test_to_file
        test_to_standard
        tearDown

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
        self.args4 = ArgParser()
        self.args5 = ArgParser()
        self.args.args_array = {"-j": True, "-G": True}
        self.args2.args_array = {"-l": True, "-G": True}
        self.args3.args_array = {"-G": True}
        self.args4.args_array = {"-G": True, "-a": True}
        self.args5.args_array = {"-j": True, "-G": True, "-g": True}
        self.ofile = "./test/unit/mongo_db_admin/tmp/get_log.txt"

    @mock.patch("mongo_db_admin.gen_libs.print_data")
    def test_to_json_flatten(self, mock_print):

        """Function:  test_to_json_flatten

        Description:  Test with going to JSON and flattening.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(
            mongo_db_admin.get_log(self.server, self.args5), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.print_data")
    def test_to_json(self, mock_print):

        """Function:  test_to_json

        Description:  Test going to JSON.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(
            mongo_db_admin.get_log(self.server, self.args), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.print_data")
    def test_to_list(self, mock_print):

        """Function:  test_to_list

        Description:  Test going to list.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(
            mongo_db_admin.get_log(self.server, self.args2), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file2")
    def test_append_to_file(self, mock_print):

        """Function:  test_append_to_file

        Description:  Test with appending to a file.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(
            mongo_db_admin.get_log(
                self.server, self.args4, ofile=self.ofile), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file2")
    def test_to_file(self, mock_print):

        """Function:  test_to_file

        Description:  Test going to file.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(
            mongo_db_admin.get_log(
                self.server, self.args3, ofile=self.ofile), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file2")
    def test_to_standard(self, mock_print):

        """Function:  test_to_standard

        Description:  Test going to standard out.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(
            mongo_db_admin.get_log(self.server, self.args3), (False, None))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
