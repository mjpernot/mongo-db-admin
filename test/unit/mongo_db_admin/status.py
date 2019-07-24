#!/usr/bin/python
# Classification (U)

"""Program:  status.py

    Description:  Unit testing of status in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/status.py

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


def run_compact():

    """Method:  run_compact

    Description:  Stub holder for run_compact function.

    Arguments:

    """

    return True


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.
        upd_srv_stat -> Stub holder for mongo_class.Server.upd_srv_stat method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"
        self.cur_mem = 1000
        self.max_mem = 10000
        self.prct_mem = 10
        self.days_up = 1
        self.cur_conn = 9
        self.max_conn = 100
        self.prct_conn = 11

    def upd_srv_stat(self):

        """Method:  upd_srv_stat

        Description:  Stub holder for mongo_class.Server.upd_srv_stat method.

        Arguments:

        """

        return True

class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_to_json_both -> Test with JSON to file and database.
        test_to_json_file -> Test with JSON to file.
        test_to_json_db -> Test with JSON to database.
        test_to_file -> Test going to file.
        test_to_standard -> Test going to standard out.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {}
        self.args_array2 = {"-j": True}

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_json_both(self, mock_db, mock_file):

        """Function:  test_to_json_both

        Description:  Test with JSON to file and database.

        Arguments:

        """

        mock_db.return_value = True
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array2,
                                               ofile="filename",
                                               class_cfg="mongo_cfg",
                                               db_tbl="db:tbl"),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    def test_to_json_file(self, mock_file):

        """Function:  test_to_json_file

        Description:  Test with JSON to file.

        Arguments:

        """

        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array2,
                                               ofile="filename"),
                         (False, None))

    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_json_db(self, mock_db):

        """Function:  test_to_json_db

        Description:  Test with JSON to database.

        Arguments:

        """

        mock_db.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array2,
                                               class_cfg="mongo_cfg",
                                               db_tbl="db:tbl"),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.print_dict")
    def test_to_file(self, mock_print):

        """Function:  test_to_file

        Description:  Test going to file.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array,
                                               ofile="Outfile"),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.display_data")
    def test_to_standard(self, mock_print):

        """Function:  test_to_standard

        Description:  Test going to standard out.

        Arguments:

        """

        mock_print.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array),
                         (False, None))


if __name__ == "__main__":
    unittest.main()
