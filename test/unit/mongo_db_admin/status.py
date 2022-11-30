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
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self, lag_time=1):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.lag_time = lag_time
        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        self.data = data

        return True

    def send_mail(self, use_mailx=False):

        """Method:  get_name

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        status = True

        if use_mailx:
            status = True

        return status


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        upd_srv_stat

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
        setUp
        test_ins_doc_failure
        test_ins_doc_success
        test_to_dict_all
        test_to_json_all
        test_to_dict_email
        test_to_json_email
        test_to_dict_both
        test_to_json_both
        test_to_json_file_flatten
        test_to_json_file
        test_to_dict_db
        test_to_json_db
        test_append_to_file
        test_to_file
        test_std_suppress
        test_to_standard

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
        self.args_array4 = {"-z": True, "-a": True}
        self.args_array5 = {"-j": True, "-z": True, "-g": True}
        self.db_tbl = "db:tbl"
        self.status = (False, "Connection Failure")
        self.errmsg = "Inserting into Mongo database:  %s" % self.status[1]

    @mock.patch("mongo_db_admin.gen_libs")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_ins_doc_failure(self, mock_db, mock_lib):

        """Function:  test_ins_doc_failure

        Description:  Test with failed insert into database.

        Arguments:

        """

        mock_db.return_value = self.status
        mock_lib.display_data.return_value = True
        mock_lib.openfile.return_value = "FileHandler"

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array3, ofile="filename",
            class_cfg="mongo_cfg", db_tbl=self.db_tbl,
            mail=self.mail), (True, self.errmsg))

    @mock.patch("mongo_db_admin.gen_libs")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_ins_doc_success(self, mock_db, mock_lib):

        """Function:  test_ins_doc_success

        Description:  Test with successful insert into database.

        Arguments:

        """

        mock_db.return_value = (True, None)
        mock_lib.display_data.return_value = True
        mock_lib.openfile.return_value = "FileHandler"

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array3, ofile="filename",
            class_cfg="mongo_cfg", db_tbl=self.db_tbl,
            mail=self.mail), (False, None))

    @mock.patch("mongo_db_admin.gen_libs")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_dict_all(self, mock_db, mock_lib):

        """Function:  test_to_dict_all

        Description:  Test with dictionary to file, database, and email.

        Arguments:

        """

        mock_db.return_value = (True, None)
        mock_lib.display_data.return_value = True
        mock_lib.openfile.return_value = "FileHandler"

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

        mock_db.return_value = (True, None)
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

        mock_db.return_value = (True, None)
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

        mock_db.return_value = (True, None)
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array2,
                                               mail=self.mail), (False, None))

    @mock.patch("mongo_db_admin.gen_libs")
    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_dict_both(self, mock_db, mock_lib):

        """Function:  test_to_dict_both

        Description:  Test with dictionary to file and database.

        Arguments:

        """

        mock_db.return_value = (True, None)
        mock_lib.display_data.return_value = True
        mock_lib.openfile.return_value = "FileHandler"

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

        mock_db.return_value = (True, None)
        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array2, ofile="filename",
            class_cfg="mongo_cfg", db_tbl=self.db_tbl), (False, None))

    @mock.patch("mongo_db_admin.gen_libs.write_file")
    def test_to_json_file_flatten(self, mock_file):

        """Function:  test_to_json_file_flatten

        Description:  Test with flatten JSON to file.

        Arguments:

        """

        mock_file.return_value = True

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array5, ofile="filename"), (False, None))

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

        mock_db.return_value = (True, None)

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array3, class_cfg="mongo_cfg",
            db_tbl=self.db_tbl), (False, None))

    @mock.patch("mongo_db_admin.mongo_libs.ins_doc")
    def test_to_json_db(self, mock_db):

        """Function:  test_to_json_db

        Description:  Test with JSON to database.

        Arguments:

        """

        mock_db.return_value = (True, None)

        self.assertEqual(mongo_db_admin.status(
            self.server, self.args_array2, class_cfg="mongo_cfg",
            db_tbl=self.db_tbl), (False, None))

    @mock.patch("mongo_db_admin.gen_libs")
    def test_append_to_file(self, mock_lib):

        """Function:  test_append_to_file

        Description:  Testing with appending data to a file.

        Arguments:

        """

        mock_lib.write_file.return_value = True
        mock_lib.openfile.return_value = "FileHandler"

        self.assertEqual(mongo_db_admin.status(self.server, self.args_array4,
                                               ofile="Outfile"), (False, None))

    @mock.patch("mongo_db_admin.gen_libs")
    def test_to_file(self, mock_lib):

        """Function:  test_to_file

        Description:  Test going to file.

        Arguments:

        """

        mock_lib.write_file.return_value = True
        mock_lib.openfile.return_value = "FileHandler"

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
