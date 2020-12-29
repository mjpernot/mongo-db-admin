#!/usr/bin/python
# Classification (U)

"""Program:  run_compact.py

    Description:  Unit testing of run_compact in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/run_compact.py

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


class Coll2(object):

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.Coll.connect method.
        coll_options -> Stub holder for mongo_class.Coll.coll_options method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return True

    def coll_options(self):

        """Method:  coll_options

        Description:  Stub holder for mongo_class.Coll.coll_options method.

        Arguments:

        """

        return {"capped": False}


class Coll(object):

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.Coll.connect method.
        coll_options -> Stub holder for mongo_class.Coll.coll_options method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return True

    def coll_options(self):

        """Method:  coll_options

        Description:  Stub holder for mongo_class.Coll.coll_options method.

        Arguments:

        """

        return {"capped": True}


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for mongo_class.DB class.

    Methods:
        __init__ -> Class initialization.
        chg_db -> Stub holder for mongo_class.DB.chg_db method.
        get_tbl_list -> Stub holder for mongo_class.DB.get_tbl_list method.
        db_cmd -> Stub holder for mongo_class.DB.db_cmd method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_name = "DatabaseName"
        self.tbl_list = []
        self.cmd_type = True
        self.dbn = None
        self.status = None
        self.com_type = None
        self.obj = None

    def chg_db(self, dbs):

        """Method:  chg_db

        Description:  Stub holder for mongo_class.DB.chg_db method.

        Arguments:
            (input) dbn -> Database name.

        """

        self.dbn = dbs

        return True

    def get_tbl_list(self, status):

        """Method:  get_tbl_list

        Description:  Stub holder for mongo_class.DB.get_tbl_list method.

        Arguments:
            (input) status -> Status of check.

        """

        self.status = status

        return self.tbl_list

    def db_cmd(self, com_type, obj):

        """Method:  db_cmd

        Description:  Stub holder for mongo_class.DB.db_cmd method.

        Arguments:
            (input) com_type -> Type of compression.
            (input) obj -> Object name.

        """

        self.com_type = com_type
        self.obj = obj
        data = {"ok": 0}

        if self.cmd_type:
            data = {"ok": 1}

        return data


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_compact_failure -> Test of compact as failure.
        test_compact_successful -> Test of compact as successful.
        test_coll_capped -> Test with collection set to capped.
        test_empty_tbl_list -> Test with empty table list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()
        self.db_name = "DatabaseName"
        self.tbl_name = ["Table3", "Table4"]

    @mock.patch("mongo_db_admin.mongo_libs.crt_coll_inst")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_compact_failure(self, mock_cmd, mock_create):

        """Function:  test_compact_failure

        Description:  Test of compact as failure.

        Arguments:

        """

        mock_cmd.return_value = True
        mock_create.return_value = Coll2()
        self.mongo.cmd_type = False

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_compact(self.mongo,
                                                        self.db_name,
                                                        self.tbl_name))

    @mock.patch("mongo_db_admin.mongo_libs.crt_coll_inst")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_compact_successful(self, mock_cmd, mock_create):

        """Function:  test_compact_successful

        Description:  Test of compact as successful.

        Arguments:

        """

        mock_cmd.return_value = True
        mock_create.return_value = Coll2()

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_compact(self.mongo,
                                                        self.db_name,
                                                        self.tbl_name))

    @mock.patch("mongo_db_admin.mongo_libs.crt_coll_inst")
    @mock.patch("mongo_db_admin.mongo_libs.disconnect")
    def test_coll_capped(self, mock_cmd, mock_create):

        """Function:  test_coll_capped

        Description:  Test with collection set to capped.

        Arguments:

        """

        mock_cmd.return_value = True
        mock_create.return_value = Coll()

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_compact(self.mongo,
                                                        self.db_name,
                                                        self.tbl_name))

    def test_empty_tbl_list(self):

        """Function:  test_empty_tbl_list

        Description:  Test with empty table list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.run_compact(self.mongo,
                                                        self.db_name))


if __name__ == "__main__":
    unittest.main()
