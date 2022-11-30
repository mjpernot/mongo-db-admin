# Classification (U)

"""Program:  process_mail.py

    Description:  Unit testing of process_mail in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/process_mail.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Third-party
import json

# Local
sys.path.append(os.getcwd())
import mongo_db_admin
import version

__version__ = version.__version__


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
            (input) use_mailx -> True|False - To use mailx command.

        """

        status = True

        if use_mailx:
            status = True

        return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mailx_default
        test_mailx_true
        test_mailx_false
        test_mail_no_indent
        test_str_to_email
        test_dict_to_email
        test_json_to_email

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.data = {"key": "value"}
        self.data2 = "Key: Value"
        self.indent = 4
        self.use_mailx = True
        self.use_mailx2 = False

    def test_mailx_default(self):

        """Function:  test_mailx_default

        Description:  Test with use_mailx option using default setting.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_mail(
                self.mail, self.data2, self.indent))

    def test_mailx_true(self):

        """Function:  test_mailx_true

        Description:  Test with use_mailx option set to True.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_mail(
                self.mail, self.data2, self.indent, self.use_mailx))

    def test_mailx_false(self):

        """Function:  test_mailx_false

        Description:  Test with use_mailx option set to False.

        Arguments:

        """

        self.assertFalse(
            mongo_db_admin.process_mail(
                self.mail, self.data2, self.indent, self.use_mailx2))

    def test_mail_no_indent(self):

        """Function:  test_mail_no_indent

        Description:  Test with dictionary to email with no indent passed.

        Arguments:

        """

        self.assertFalse(mongo_db_admin.process_mail(self.mail, self.data))

    def test_str_to_email(self):

        """Function:  test_str_to_email

        Description:  Test with string to email.

        Arguments:

        """

        self.assertFalse(mongo_db_admin.process_mail(self.mail, self.data2,
                                                     self.indent))

    def test_dict_to_email(self):

        """Function:  test_dict_to_email

        Description:  Test with dictionary to email.

        Arguments:

        """

        self.assertFalse(mongo_db_admin.process_mail(self.mail, self.data,
                                                     self.indent))

    def test_json_to_email(self):

        """Function:  test_json_to_email

        Description:  Test with JSON to email.

        Arguments:

        """

        self.data = json.dumps(self.data, indent=4)

        self.assertFalse(mongo_db_admin.process_mail(self.mail, self.data,
                                                     self.indent))


if __name__ == "__main__":
    unittest.main()
