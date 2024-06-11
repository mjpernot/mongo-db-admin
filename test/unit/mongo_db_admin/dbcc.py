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
import mongo_db_admin
import version

__version__ = version.__version__


def run_dbcc():

    """Method:  run_dbcc

    Description:  Stub holder for run_dbcc function.

    Arguments:

    """

    return True


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
        test_dbcc2
        test_dbcc

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args.args_array = {"-D": "Optionsetting", "-t": "option"}

    @mock.patch("mongo_db_admin.process_request")
    def test_dbcc2(self, mock_process):

        """Function:  test_dbcc2

        Description:  Test dbcc function.

        Arguments:

        """

        mock_process.return_value = (True, "Error Message")

        self.assertEqual(
            mongo_db_admin.dbcc(
                self.server, self.args), (True, "Error Message"))

    @mock.patch("mongo_db_admin.process_request")
    def test_dbcc(self, mock_process):

        """Function:  test_dbcc

        Description:  Test dbcc function.

        Arguments:

        """

        mock_process.return_value = (False, None)

        self.assertEqual(
            mongo_db_admin.dbcc(self.server, self.args), (False, None))


if __name__ == "__main__":
    unittest.main()
