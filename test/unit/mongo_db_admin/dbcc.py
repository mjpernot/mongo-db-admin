#!/usr/bin/python
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


def run_dbcc():

    """Method:  run_dbcc

    Description:  Stub holder for run_dbcc function.

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

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_dbcc -> Test dbcc function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-D": "Optionsetting", "-t": "option"}

    @mock.patch("mongo_db_admin.process_request")
    def test_dbcc(self, mock_process):

        """Function:  test_dbcc

        Description:  Test dbcc function.

        Arguments:

        """

        mock_process.return_value = True

        self.assertEqual(mongo_db_admin.dbcc(self.server, self.args_array),
                         (False, None))


if __name__ == "__main__":
    unittest.main()
