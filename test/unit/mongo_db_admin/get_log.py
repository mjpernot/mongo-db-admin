#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_admin
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.
        adm_cmd -> Stub holder for mongo_class.Server.adm_cmd method.

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
        setUp -> Initialize testing environment.
        test_to_json_flatten -> Test with going to JSON and flattening.
        test_to_json -> Test going to JSON.
        test_to_list -> Test going to list.
        test_append_to_file -> Test with appending to a file.
        test_to_file -> Test going to file.
        test_to_standard -> Test going to standard out.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-j": True, "-G": True}
        self.args_array2 = {"-l": True, "-G": True}
        self.args_array3 = {"-G": True}
        self.args_array4 = {"-G": True, "-a": True}
        self.args_array5 = {"-j": True, "-G": True, "-g": True}
        self.ofile = "./test/unit/mongo_db_admin/tmp/get_log.txt"

    @mock.patch("mongo_db_admin.gen_libs.print_data")
    def test_to_json_flatten(self, mock_print):

        """Function:  test_to_json_flatten

        Description:  Test with going to JSON and flattening.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(mongo_db_admin.get_log(self.server, self.args_array5),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.print_data")
    def test_to_json(self, mock_print):

        """Function:  test_to_json

        Description:  Test going to JSON.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(mongo_db_admin.get_log(self.server, self.args_array),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.print_data")
    def test_to_list(self, mock_print):

        """Function:  test_to_list

        Description:  Test going to list.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(mongo_db_admin.get_log(self.server, self.args_array2),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file2")
    def test_append_to_file(self, mock_print):

        """Function:  test_append_to_file

        Description:  Test with appending to a file.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(mongo_db_admin.get_log(self.server, self.args_array4,
                                                ofile=self.ofile),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file2")
    def test_to_file(self, mock_print):

        """Function:  test_to_file

        Description:  Test going to file.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(mongo_db_admin.get_log(self.server, self.args_array3,
                                                ofile=self.ofile),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file2")
    def test_to_standard(self, mock_print):

        """Function:  test_to_standard

        Description:  Test going to standard out.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(mongo_db_admin.get_log(self.server, self.args_array3),
                         (False, None))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
