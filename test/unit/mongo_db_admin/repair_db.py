#!/usr/bin/python
# Classification (U)

"""Program:  repair_db.py

    Description:  Unit testing of repair_db in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/repair_db.py

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


def run_repair():

    """Method:  run_repair

    Description:  Stub holder for run_repair function.

    Arguments:

    """

    return True


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_repair_db2 -> Test repair_db function.
        test_repair_db -> Test repair_db function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-R": "Optionsetting"}

    @mock.patch("mongo_db_admin.process_request")
    def test_repair_db2(self, mock_process):

        """Function:  test_repair_db2

        Description:  Test repair_db function.

        Arguments:

        """

        mock_process.return_value = (True, "Error Message")

        self.assertEqual(
            mongo_db_admin.repair_db(
                self.server, self.args_array), (True, "Error Message"))

    @mock.patch("mongo_db_admin.process_request")
    def test_repair_db(self, mock_process):

        """Function:  test_repair_db

        Description:  Test repair_db function.

        Arguments:

        """

        mock_process.return_value = (False, None)

        self.assertEqual(
            mongo_db_admin.repair_db(
                self.server, self.args_array), (False, None))


if __name__ == "__main__":
    unittest.main()
