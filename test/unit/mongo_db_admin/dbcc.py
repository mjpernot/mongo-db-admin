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

        self.args_array = {"-c": "mongo", "-d": "config", "-D": []}

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


class Mongo():

    """Class:  Mongo

    Description:  Class stub holder for mongo_class.DB class.

    Methods:
        __init__
        connect
        chg_db
        validate_tbl

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_name = "DatabaseName"
        self.name = "ServerName"
        self.dbn = None
        self.status = True
        self.errmsg = None
        self.tbl = None
        self.scan = False
        self.status2 = True
        self.err2 = None
        self.valid2 = True

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Server.connect method.

        Arguments:

        """

        return self.status, self.errmsg

    def chg_db(self, dbs):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.DB.chg_db method.

        Arguments:

        """

        self.dbn = dbs

        return True

    def validate_tbl(self, tbl, scan):

        """Method:  validate_tbl

        Description:  Stub holder for mongo_class.DB.validate_tbl method.

        Arguments:

        """

        self.tbl = tbl
        self.scan = scan

        return (self.status2, {"valid": self.valid2, "errors": self.err2})


class Cfg():                                            # pylint:disable=R0903

    """Class:  Cfg

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.ign_dbs = ["admin"]


class Cfg2():                                           # pylint:disable=R0903

    """Class:  Cfg

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_data_out_failed
        test_dbcc_failure2
        test_dbcc_failure
        test_dbcc_success
        test_sys_dbs
        test_cfg_ign_dbs
        test_mongo_fail

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()
        self.args = ArgParser()
        self.cfg = Cfg()
        self.cfg2 = Cfg2()
        self.db_tbl = {"db": ["tbl"]}
        self.status = (True, None)
        self.status2 = (False, "Data Out Failed")
        self.results = (True, None)
        self.results2 = (False, "Connection to Mongo DB:  Connection Failed")
        self.results3 = (False, "dbcc: Error encountered: Data Out Failed")

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_data_out_failed(self, mock_mongo, mock_module, mock_dbtbl,
                             mock_out):

        """Function:  test_data_out_failed

        Description:  Test a failure in data_out call.

        Arguments:

        """

        mock_mongo.return_value = self.mongo
        mock_module.return_value = self.cfg
        mock_dbtbl.return_value = self.db_tbl
        mock_out.return_value = self.status2

        self.assertEqual(
            mongo_db_admin.dbcc(self.mongo, self.args), self.results3)

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_dbcc_failure2(self, mock_mongo, mock_module, mock_dbtbl,
                           mock_out):

        """Function:  test_dbcc_failure2

        Description:  Test with a failed dbcc run.

        Arguments:

        """

        self.mongo.valid2 = False
        self.mongo.err2 = "Error Message"

        mock_mongo.return_value = self.mongo
        mock_module.return_value = self.cfg
        mock_dbtbl.return_value = self.db_tbl
        mock_out.return_value = self.status

        self.assertEqual(
            mongo_db_admin.dbcc(self.mongo, self.args), self.results)

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_dbcc_failure(self, mock_mongo, mock_module, mock_dbtbl, mock_out):

        """Function:  test_dbcc_failure

        Description:  Test with a failed dbcc run.

        Arguments:

        """

        self.mongo.status2 = False
        self.mongo.valid2 = False
        self.mongo.err2 = "Error Message"

        mock_mongo.return_value = self.mongo
        mock_module.return_value = self.cfg
        mock_dbtbl.return_value = self.db_tbl
        mock_out.return_value = self.status

        self.assertEqual(
            mongo_db_admin.dbcc(self.mongo, self.args), self.results)

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_dbcc_success(self, mock_mongo, mock_module, mock_dbtbl, mock_out):

        """Function:  test_dbcc_success

        Description:  Test with a successful dbcc run.

        Arguments:

        """

        mock_mongo.return_value = self.mongo
        mock_module.return_value = self.cfg
        mock_dbtbl.return_value = self.db_tbl
        mock_out.return_value = self.status

        self.assertEqual(
            mongo_db_admin.dbcc(self.mongo, self.args), self.results)

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_sys_dbs(self, mock_mongo, mock_module, mock_dbtbl, mock_out):

        """Function:  test_sys_dbs

        Description:  Test using the default sys_dbs global variable.

        Arguments:

        """

        mock_mongo.return_value = self.mongo
        mock_module.return_value = self.cfg2
        mock_dbtbl.return_value = {}
        mock_out.return_value = self.status

        self.assertEqual(
            mongo_db_admin.dbcc(self.mongo, self.args), self.results)

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_cfg_ign_dbs(self, mock_mongo, mock_module, mock_dbtbl, mock_out):

        """Function:  test_mongo_fail

        Description:  Test using config ignore databases entry.

        Arguments:

        """

        mock_mongo.return_value = self.mongo
        mock_module.return_value = self.cfg
        mock_dbtbl.return_value = {}
        mock_out.return_value = self.status

        self.assertEqual(
            mongo_db_admin.dbcc(self.mongo, self.args), self.results)

    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    def test_mongo_fail(self, mock_mongo):

        """Function:  test_mongo_fail

        Description:  Test mongo connection fails.

        Arguments:

        """

        self.mongo.status = False
        self.mongo.errmsg = "Connection Failed"

        mock_mongo.return_value = self.mongo

        self.assertEqual(
            mongo_db_admin.dbcc(self.mongo, self.args), self.results2)


if __name__ == "__main__":
    unittest.main()
