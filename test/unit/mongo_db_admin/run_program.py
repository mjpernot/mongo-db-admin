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


def dbcc(server, args_array, ofile, db_tbl, class_cfg, **kwargs):

    """Method:  dbcc

    Description:  Stub holder for dbcc function.

    Arguments:
        (input) server -> Mongo instance.
        (input) args_array -> Dict of command line options and values.
        (input) db_tbl -> Database and table names.
        (input) class_cfg -> Class configuration file.
        (input) kwargs:
            mail => Mail instance.

    """

    flag = True
    errmsg = "ErrorMessage"
    mail = kwargs.get("mail", None)

    if server and args_array and ofile and db_tbl and class_cfg and mail:
        flag = True
        errmsg = "ErrorMessage"

    return flag, errmsg


def defrag(server, args_array, ofile, db_tbl, class_cfg, **kwargs):

    """Method:  defrag

    Description:  Stub holder for defrag function.

    Arguments:
        (input) server -> Mongo instance.
        (input) args_array -> Dict of command line options and values.
        (input) db_tbl -> Database and table names.
        (input) class_cfg -> Class configuration file.
        (input) kwargs:
            mail => Mail instance.

    """

    flag = False
    errmsg = None
    mail = kwargs.get("mail", None)

    if server and args_array and ofile and db_tbl and class_cfg and mail:
        flag = False
        errmsg = None

    return flag, errmsg


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
        test_email
        test_cfg
        test_no_cfg

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
            self.assertFalse(mongo_db_admin.run_program(self.args_array,
                                                        self.func_names))

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_connection_successful(self, mock_mongo):

        """Function:  test_connection_successful

        Description:  Test with successful connection.

        Arguments:

        """

        mock_mongo.return_value = self.server

        self.assertFalse(mongo_db_admin.run_program(self.args_array,
                                                    self.func_names))

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_func_failure(self, mock_mongo, mock_load):

        """Function:  test_func_failure

        Description:  Test with function returning error message.

        Arguments:

        """

        mock_mongo.return_value = self.server
        mock_load.return_value = "RepConfig"

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_program(self.args_array2,
                                                        self.func_names2))

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.gen_class.setup_mail")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_email(self, mock_mongo, mock_load, mock_mail):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_mongo.return_value = self.server
        mock_load.return_value = "RepConfig"
        mock_mail.return_value = "EmailInstance"

        self.assertFalse(mongo_db_admin.run_program(self.args_array3,
                                                    self.func_names))

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_cfg(self, mock_mongo, mock_load):

        """Function:  test_cfg

        Description:  Test with configuration file.

        Arguments:

        """

        mock_mongo.return_value = self.server
        mock_load.return_value = "RepConfig"

        self.assertFalse(mongo_db_admin.run_program(self.args_array2,
                                                    self.func_names))

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_no_cfg(self, mock_mongo):

        """Function:  test_no_cfg

        Description:  Test with no configuration file.

        Arguments:

        """

        mock_mongo.return_value = self.server

        self.assertFalse(mongo_db_admin.run_program(self.args_array,
                                                    self.func_names))


if __name__ == "__main__":
    unittest.main()
