#!/usr/bin/python
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


def dbcc(server, args_array, ofile, db_tbl, class_cfg, **kwargs):

    """Method:  dbcc

    Description:  Stub holder for dbcc function.

    Arguments:
        (input) server -> Mongo instance.
        (input) args_array -> Dict of command line options and values.
        (input) db_tbl -> Database and table names.
        (input) class_cfg -> Class configuration file.

    """

    return True, "ErrorMessage"


def defrag(server, args_array, ofile, db_tbl, class_cfg, **kwargs):

    """Method:  defrag

    Description:  Stub holder for defrag function.

    Arguments:
        (input) server -> Mongo instance.
        (input) args_array -> Dict of command line options and values.
        (input) db_tbl -> Database and table names.
        (input) class_cfg -> Class configuration file.

    """

    return False, None


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.Server.connect method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Server.connect method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_func_failure -> Test with function returning error message.
        test_email -> Test with email option.
        test_cfg -> Test with configuration file.
        test_no_cfg -> Test with no configuration file.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-c": True, "-d": True, "-C": True}
        self.args_array2 = {"-c": True, "-d": True, "-C": True, "-m": True}
        self.args_array3 = {"-c": True, "-d": True, "-C": True, "-m": True,
                            "-e": "ToEmail", "-s": "SubjectLine"}
        self.func_dict = {"-C": defrag}
        self.func_dict2 = {"-C": dbcc}

    @mock.patch("mongo_db_admin.sys.exit")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.cmds_gen.disconnect")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_func_failure(self, mock_mongo, mock_conn, mock_load, mock_exit):

        """Function:  test_func_failure

        Description:  Test with function returning error message.

        Arguments:

        """

        mock_mongo.return_value = self.server
        mock_conn.return_value = True
        mock_load.return_value = "RepConfig"
        mock_exit.return_value = True

        self.assertFalse(mongo_db_admin.run_program(self.args_array2,
                                                    self.func_dict2))

    @mock.patch("mongo_db_admin.gen_class.setup_mail")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.cmds_gen.disconnect")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_email(self, mock_mongo, mock_conn, mock_load, mock_mail):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_mongo.return_value = self.server
        mock_conn.return_value = True
        mock_load.return_value = "RepConfig"
        mock_mail.return_value = "EmailInstance"

        self.assertFalse(mongo_db_admin.run_program(self.args_array3,
                                                    self.func_dict))

    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.cmds_gen.disconnect")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_cfg(self, mock_mongo, mock_conn, mock_load):

        """Function:  test_cfg

        Description:  Test with configuration file.

        Arguments:

        """

        mock_mongo.return_value = self.server
        mock_conn.return_value = True
        mock_load.return_value = "RepConfig"

        self.assertFalse(mongo_db_admin.run_program(self.args_array2,
                                                    self.func_dict))

    @mock.patch("mongo_db_admin.cmds_gen.disconnect")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_no_cfg(self, mock_mongo, mock_conn):

        """Function:  test_no_cfg

        Description:  Test with no configuration file.

        Arguments:

        """

        mock_mongo.return_value = self.server
        mock_conn.return_value = True

        self.assertFalse(mongo_db_admin.run_program(self.args_array,
                                                    self.func_dict))


if __name__ == "__main__":
    unittest.main()
