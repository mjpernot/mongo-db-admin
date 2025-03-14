# Classification (U)

"""Program:  get_json_template.py

    Description:  Unit testing of get_json_template in mongo_db_admin.py.

    Usage:
        python test/unit/mongo_db_admin/get_json_template.py
        python3 test/unit/mongo_db_admin/get_json_template.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_db_admin                           # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                                         # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_for_dtg
        test_for_servername

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.results = "ServerName"

    def test_for_dtg(self):

        """Function:  test_for_dtg

        Description:  Test for date time group.

        Arguments:

        """

        self.assertIn("AsOf", mongo_db_admin.get_json_template(self.server))

    def test_for_servername(self):

        """Function:  test_for_servername

        Description:  Test for server name.

        Arguments:

        """

        self.assertEqual(
            mongo_db_admin.get_json_template(self.server)["Server"],
            self.results)


if __name__ == "__main__":
    unittest.main()
