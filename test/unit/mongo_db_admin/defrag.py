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

        self.args_array = {"-c": "mongo", "-d": "config", "-C": list()}

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
        connect
        chg_db

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"
        self.status = True
        self.errmsg = None
        self.dbs = None

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Server.connect method.

        Arguments:

        """

        return self.status, self.errmsg

    def chg_db(self, dbs):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.Server.chg_db method.

        Arguments:

        """

        self.dbs = dbs


class Cfg(object):

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


class Cfg2(object):

    """Class:  Cfg2

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_data_out_failed
        test_compact_fail
        test_compact_successful
        test_connection_true
        test_connection_failed
        test_no_setname
        test_is_master

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.coll = Server()
        self.args = ArgParser()
        self.cfg = Cfg()
        self.cfg2 = Cfg2()
        self.ismaster = {"ismaster": False}
        self.ismaster2 = {"ismaster": True, "setName": True}
        self.db_dict = dict()
        self.db_dict2 = {"db": ["tbl"]}
        self.data_out = (True, None)
        self.data_out2 = (False, "Data Out Failure")
        err_msg = "Warning: Cannot defrag the Master in a ReplicaSet."
        err_msg2 = "Connection to Mongo DB:  Failed Connection"
        err_msg3 = "defrag: Error encountered: Data Out Failure"
        self.errmsg = (True, None)
        self.errmsg2 = (False, err_msg)
        self.errmsg3 = (False, err_msg2)
        self.errmsg4 = (False, err_msg3)

    @mock.patch("mongo_db_admin.compact", mock.Mock(return_value="Good"))
    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.mongo_libs.crt_coll_inst")
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    def test_data_out_failed(self, mock_fetch, mock_mongo, mock_load,
                             mock_dbtbl, mock_data, mock_coll):

        """Function:  test_data_out_failed

        Description:  Test with data_out failing.

        Arguments:

        """

        mock_fetch.return_value = self.ismaster
        mock_mongo.return_value = self.server
        mock_load.reuturn_value = self.cfg
        mock_dbtbl.return_value = self.db_dict2
        mock_data.return_value = self.data_out2
        mock_coll = self.coll

        self.assertEqual(
            mongo_db_admin.defrag(self.server, self.args), self.errmsg4)

    @mock.patch("mongo_db_admin.compact", mock.Mock(return_value="Good"))
    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.mongo_libs.crt_coll_inst")
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    def test_compact_fail(self, mock_fetch, mock_mongo, mock_load, mock_dbtbl,
                          mock_data, mock_coll):

        """Function:  test_compact_fail

        Description:  Test with failed compact.

        Arguments:

        """

        self.coll.status = False
        self.coll.errmsg = "Failed Compact"

        mock_fetch.return_value = self.ismaster
        mock_mongo.return_value = self.server
        mock_load.reuturn_value = self.cfg
        mock_dbtbl.return_value = self.db_dict2
        mock_data.return_value = self.data_out
        mock_coll = self.coll

        self.assertEqual(
            mongo_db_admin.defrag(self.server, self.args), self.errmsg)

    @mock.patch("mongo_db_admin.compact", mock.Mock(return_value="Good"))
    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.mongo_libs.crt_coll_inst")
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    def test_compact_successful(self, mock_fetch, mock_mongo, mock_load,
                                mock_dbtbl, mock_data, mock_coll):

        """Function:  test_compact_successful

        Description:  Test with successful compact.

        Arguments:

        """

        mock_fetch.return_value = self.ismaster
        mock_mongo.return_value = self.server
        mock_load.reuturn_value = self.cfg
        mock_dbtbl.return_value = self.db_dict2
        mock_data.return_value = self.data_out
        mock_coll = self.coll

        self.assertEqual(
            mongo_db_admin.defrag(self.server, self.args), self.errmsg)

    @mock.patch("mongo_db_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_admin.data_out")
    @mock.patch("mongo_db_admin.get_db_tbl")
    @mock.patch("mongo_db_admin.gen_libs.load_module")
    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    def test_connection_true(self, mock_fetch, mock_mongo, mock_load,
                             mock_dbtbl, mock_data):

        """Function:  test_connection_true

        Description:  Test with mongo connection successful.

        Arguments:

        """

        mock_fetch.return_value = self.ismaster
        mock_mongo.return_value = self.server
        mock_load.reuturn_value = self.cfg
        mock_dbtbl.return_value = self.db_dict
        mock_data.return_value = self.data_out

        self.assertEqual(
            mongo_db_admin.defrag(self.server, self.args), self.errmsg)

    @mock.patch("mongo_db_admin.mongo_libs.create_instance")
    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    def test_connection_failed(self, mock_fetch, mock_mongo):

        """Function:  test_connection_failed

        Description:  Test with mongo connection failed.

        Arguments:

        """

        self.server.status = False
        self.server.errmsg = "Failed Connection"

        mock_fetch.return_value = self.ismaster
        mock_mongo.return_value = self.server

        self.assertEqual(
            mongo_db_admin.defrag(self.server, self.args), self.errmsg3)

    @mock.patch("mongo_db_admin.mongo_class.fetch_ismaster")
    def test_is_master(self, mock_fetch):

        """Function:  test_is_master

        Description:  Test with database being the master.

        Arguments:

        """

        mock_fetch.return_value = self.ismaster2

        self.assertEqual(
            mongo_db_admin.defrag(self.server, self.args), self.errmsg2)


if __name__ == "__main__":
    unittest.main()
