# Classification (U)

"""Program:  compact.py

    Description:  Unit testing of compact in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/compact.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        __init__
        connect
        coll_options

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

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return self.status, self.errmsg

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
        __init__
        connect
        coll_options

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

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return self.status, self.errmsg

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
        __init__
        chg_db
        get_tbl_list
        db_cmd

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
        setUp
        test_compact_failure
        test_compact_successful
        test_coll_capped
        test_empty_tbl_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()
        self.coll = Coll()
        self.coll2 = Coll2()
        self.tbl_name = "TableName"

    def test_compact_failure(self):

        """Function:  test_compact_failure

        Description:  Test of compact as failure.

        Arguments:

        """

        self.mongo.cmd_type = False

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.compact(
                self.mongo, self.coll2, self.tbl_name))

    def test_compact_successful(self):

        """Function:  test_compact_successful

        Description:  Test of compact as successful.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.compact(
                self.mongo, self.coll2, self.tbl_name))

    def test_coll_capped(self):

        """Function:  test_coll_capped

        Description:  Test with collection set to capped.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_admin.compact(
                self.mongo, self.coll, self.tbl_name))


if __name__ == "__main__":
    unittest.main()
