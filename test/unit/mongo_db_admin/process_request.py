#!/usr/bin/python
# Classification (U)

"""Program:  process_request.py

    Description:  Unit testing of process_request in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/process_request.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def func_name(mongo, dbn, tbl_list=None, **kwargs):

    """Method:  func_name

    Description:  Stub holder for genertic function.

    Arguments:
        (input) mongo -> Mongo instance.
        (input) dbn -> Database name.
        (input) tbl_list -> Table name list.
        (input) kwargs:
            mail => Mail instance.

    """

    status = True
    mail = kwargs.get("mail", None)

    if mongo and dbn and tbl_list and mail:
        status = True

    return status


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        fetch_dbs

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "Server name"
        self.user = "User name"
        self.japd = "User pwd"
        self.host = "Host name"
        self.port = 27017
        self.auth = "Auth type"
        self.conf_file = "Config file name"
        self.db_list = ["DB1", "DB2"]
        self.auth_db = "admin"

    def fetch_dbs(self):

        """Method:  fetch_dbs

        Description:  Stub holder for mongo_class.Server.fetch_dbs method.

        Arguments:

        """

        return self.db_list


class Server2(object):

    """Class:  Server2

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        fetch_dbs

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "Server name2"
        self.user = "User name2"
        self.japd = "User pwd2"
        self.host = "Host name2"
        self.port = 27017
        self.auth = "Auth type2"
        self.conf_file = "Config file name2"
        self.db_list = ["DB3", "DB4"]
        self.auth_db = "admin"
        self.auth_mech = "MONGODB-CR"

    def fetch_dbs(self):

        """Method:  fetch_dbs

        Description:  Stub holder for mongo_class.Server.fetch_dbs method.

        Arguments:

        """

        return self.db_list


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for mongo_class.DB class.

    Methods:
        __init__
        connect
        chg_db
        get_tbl_list

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.dbn = None
        self.state = True
        self.errmsg = None
        self.tbl_list = ["Table1", "Table2"]

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.DB.connect method.

        Arguments:

        """

        return self.state, self.errmsg

    def chg_db(self, dbs):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.DB.chg_db method.

        Arguments:
            (input) dbn -> Database name.

        """

        self.dbn = dbs

        return True

    def get_tbl_list(self):

        """Method:  get_tbl_list

        Description:  Stub holder for mongo_class.DB.get_tbl_list method.

        Arguments:

        """

        return self.tbl_list


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_auth_mech
        test_tbl_list4
        test_tbl_list3
        test_tbl_list2
        test_connection_failure
        test_connection_success
        test_tbl_list
        test_db_list
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.server2 = Server2()
        self.mongo = Mongo()
        self.func_name = func_name
        self.db_name = ["DB1"]
        self.tbl_name = ["Table1", "Table2"]
        self.tbl_name2 = ["Table2"]
        self.tbl_name3 = ["Table2", "Table3"]
        self.tbl_name4 = ["Table3", "Table4"]
        self.err_flag = False
        self.err_flag2 = True
        self.err_msg = None
        msg = "Connection Error"
        self.err_msg2 = "Connection to Mongo DB:  %s" % msg

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_auth_mech(self, mock_conn, mock_db):

        """Function:  test_auth_mech

        Description:  Test with auth_mech attribute present.

        Arguments:

        """

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.process_request(self.server2, self.func_name),
            (self.err_flag, self.err_msg))

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_tbl_list4(self, mock_conn, mock_db):

        """Function:  test_tbl_list4

        Description:  Test with no match table list.

        Arguments:

        """

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_admin.process_request(
                    self.server, self.func_name, self.db_name, self.tbl_name4),
                (self.err_flag, self.err_msg))

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_tbl_list3(self, mock_conn, mock_db):

        """Function:  test_tbl_list3

        Description:  Test with partial table list.

        Arguments:

        """

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.process_request(
                self.server, self.func_name, self.db_name, self.tbl_name3),
            (self.err_flag, self.err_msg))

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_tbl_list2(self, mock_conn, mock_db):

        """Function:  test_tbl_list2

        Description:  Test with partial table list.

        Arguments:

        """

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.process_request(
                self.server, self.func_name, self.db_name, self.tbl_name2),
            (self.err_flag, self.err_msg))

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_connection_failure(self, mock_conn, mock_db):

        """Function:  test_connection_failure

        Description:  Test with failed connection.

        Arguments:

        """

        self.mongo.state = False
        self.mongo.errmsg = "Connection Error"

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.process_request(self.server, self.func_name),
            (self.err_flag2, self.err_msg2))

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_connection_success(self, mock_conn, mock_db):

        """Function:  test_connection_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.process_request(self.server, self.func_name),
            (self.err_flag, self.err_msg))

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_tbl_list(self, mock_conn, mock_db):

        """Function:  test_tbl_list

        Description:  Test with table list.

        Arguments:

        """

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.process_request(
                self.server, self.func_name, self.db_name, self.tbl_name),
            (self.err_flag, self.err_msg))

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_db_list(self, mock_conn, mock_db):

        """Function:  test_db_list

        Description:  Test with database list.

        Arguments:

        """

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.process_request(
                self.server, self.func_name, self.db_name),
            (self.err_flag, self.err_msg))

    @mock.patch("mongo_db_admin.mongo_class.DB")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_default(self, mock_conn, mock_db):

        """Function:  test_default

        Description:  Test with default arguments.

        Arguments:

        """

        mock_conn.return_value = True
        mock_db.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.process_request(self.server, self.func_name),
            (self.err_flag, self.err_msg))


if __name__ == "__main__":
    unittest.main()
