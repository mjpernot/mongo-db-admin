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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__ -> Class initialization.
        add_2_msg -> Stub method holder for Mail.add_2_msg.
        send_mail -> Stub method holder for Mail.send_mail.

    """

    def __init__(self, lag_time=1):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        pass

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        return True

    def send_mail(self):

        """Method:  get_name

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        return True


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

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

    Methods:
        setUp -> Initialize testing environment.
        test_to_dict_all -> Test with dictionary to file, database, and email.
        test_to_json_all -> Test with JSON to file, database, and email.
        test_to_dict_email -> Test with dictionary to email.
        test_to_json_email -> Test with JSON to email.
        test_to_dict_both -> Test with dictionary to file and database.
        test_to_json_both -> Test with JSON to file and database.
        test_to_json_file -> Test with JSON to file.
        test_to_dict_db -> Test with dictionary to database.
        test_to_json_db -> Test with JSON to database.
        test_to_file -> Test going to file.
        test_std_suppress -> Test with standard out suppressed.
        test_to_standard -> Test going to standard out.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.mail = Mail()
        self.args_array = {}
        self.args_array2 = {"-j": True, "-z": True}
        self.args_array3 = {"-z": True}
        self.db_tbl = "db:tbl"

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_dict_all(self, mock_db, mock_file):

        """Function:  test_to_dict_all

        Description:  Test with dictionary to file, database, and email.

        Arguments:

        """

        mock_db.return_value = True
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array3, ofile="filename",
            class_cfg="mongo_cfg", db_tbl=self.db_tbl,
            mail=self.mail), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_json_all(self, mock_db, mock_file):

        """Function:  test_to_json_all

        Description:  Test with JSON to file, database, and email.

        Arguments:

        """

        mock_db.return_value = True
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array2, ofile="filename",
            class_cfg="mongo_cfg", db_tbl=self.db_tbl,
            mail=self.mail), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_dict_email(self, mock_db, mock_file):

        """Function:  test_to_dict_email

        Description:  Test with dictionary to email.

        Arguments:

        """

        mock_db.return_value = True
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array3,
                                               mail=self.mail), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_json_email(self, mock_db, mock_file):

        """Function:  test_to_json_email

        Description:  Test with JSON to email.

        Arguments:

        """

        mock_db.return_value = True
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array2,
                                               mail=self.mail), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_dict_both(self, mock_db, mock_file):

        """Function:  test_to_dict_both

        Description:  Test with dictionary to file and database.

        Arguments:

        """

        mock_db.return_value = True
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array3, ofile="filename",
            class_cfg="mongo_cfg", db_tbl=self.db_tbl), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_json_both(self, mock_db, mock_file):

        """Function:  test_to_json_both

        Description:  Test with JSON to file and database.

        Arguments:

        """

        mock_db.return_value = True
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array2, ofile="filename",
            class_cfg="mongo_cfg", db_tbl=self.db_tbl), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    def test_to_json_file(self, mock_file):

        """Function:  test_to_json_file

        Description:  Test with JSON to file.

        Arguments:

        """

        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array2, ofile="filename"), (False, None))

    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_dict_db(self, mock_db):

        """Function:  test_to_dict_db

        Description:  Test with dictionary to database.

        Arguments:

        """

        mock_db.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array3, class_cfg="mongo_cfg",
            db_tbl=self.db_tbl), (False, None))

    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_json_db(self, mock_db):

        """Function:  test_to_json_db

        Description:  Test with JSON to database.

        Arguments:

        """

        mock_db.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array2, class_cfg="mongo_cfg",
            db_tbl=self.db_tbl), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    def test_to_file(self, mock_file):

        """Function:  test_to_file

        Description:  Test going to file.

        Arguments:

        """

        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array3,
                                               ofile="Outfile"), (False, None))

    def test_std_suppress(self):

        """Function:  test_std_suppress

        Description:  Test with standard out suprressed.

        Arguments:

        """

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array3),
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
