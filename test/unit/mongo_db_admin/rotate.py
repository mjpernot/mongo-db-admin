#!/usr/bin/python
# Classification (U)

"""Program:  rotate.py

    Description:  Unit testing of rotate in mongo_db_admin.py.

    Usage:
        test/unit/mongo_db_admin/rotate.py

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


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.
        adm_cmd -> Stub holder for mongo_class.Server.adm_cmd method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None

    def adm_cmd(self, cmd):

        """Method:  adm_cmd

        Description:  Stub holder for mongo_class.Server.adm_cmd method.

        Arguments:
            (input) cmd -> Database command.

        """

        self.cmd = cmd

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_compress -> Test with compression option.
        test_too_many_logs -> Test with too many logs to rotate.
        test_rotate -> Test rotate function.
        test_file_chk_fail -> Test going to file.
        test_no_log_dir -> Test with no log directory passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {}
        self.args_array2 = {"-n": "/path"}
        self.args_array3 = {"-n": "/path", "-p": True}
        self.filepath = "/dir/path/filename"

    @mock.patch("mongo_db_admin.mongo_class.fetch_cmd_line")
    @mock.patch("mongo_db_admin.gen_libs")
    def test_compress(self, mock_lib, mock_fetch):

        """Function:  test_compress

        Description:  Test with compression option.

        Arguments:

        """

        mock_lib.chk_crt_dir.return_value = (True, None)
        mock_lib.dir_file_match.side_effect = [["File1", "File2"],
                                               ["File1", "File2"]]
        mock_lib.mv_file.return_value = True
        mock_lib.is_missing_lists.return_value = ["File1"]
        mock_lib.compress.return_value = True
        mock_fetch.return_value = {"parsed": {"systemLog":
                                              {"path": self.filepath}}}

        self.assertEqual(mongo_db_admin.rotate(self.server, self.args_array3),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.is_missing_lists")
    @mock.patch("mongo_db_admin.gen_libs.dir_file_match")
    @mock.patch("mongo_db_admin.mongo_class.fetch_cmd_line")
    @mock.patch("mongo_db_admin.gen_libs.chk_crt_dir")
    def test_too_many_logs(self, mock_check, mock_fetch, mock_match,
                           mock_diff):

        """Function:  test_too_many_logs

        Description:  Test with too many logs to rotate.

        Arguments:

        """

        err_msg = "Error:  Too many files to move: ['File1', 'File2']"
        mock_check.return_value = (True, None)
        mock_fetch.return_value = {"parsed": {"systemLog":
                                              {"path": self.filepath}}}
        mock_match.side_effect = [["File1", "File2"], ["File1"]]
        mock_diff.return_value = ["File1", "File2"]

        self.assertEqual(mongo_db_admin.rotate(self.server, self.args_array2),
                         (True, err_msg))

    @mock.patch("mongo_db_admin.gen_libs.is_missing_lists")
    @mock.patch("mongo_db_admin.gen_libs.mv_file")
    @mock.patch("mongo_db_admin.gen_libs.dir_file_match")
    @mock.patch("mongo_db_admin.mongo_class.fetch_cmd_line")
    @mock.patch("mongo_db_admin.gen_libs.chk_crt_dir")
    def test_rotate(self, mock_check, mock_fetch, mock_match, mock_mv,
                    mock_diff):

        """Function:  test_rotate

        Description:  Test rotate function.

        Arguments:

        """

        mock_check.return_value = (True, None)
        mock_fetch.return_value = {"parsed": {"systemLog":
                                              {"path": self.filepath}}}
        mock_match.side_effect = [["File1", "File2"], ["File1", "File2"]]
        mock_mv.return_value = True
        mock_diff.return_value = ["File1"]

        self.assertEqual(mongo_db_admin.rotate(self.server, self.args_array2),
                         (False, None))

    @mock.patch("mongo_db_admin.gen_libs.chk_crt_dir")
    def test_file_chk_fail(self, mock_check):

        """Function:  test_file_chk_fail

        Description:  Test with file checking fails.

        Arguments:

        """

        mock_check.return_value = (False, "ErrorMsg")

        self.assertEqual(mongo_db_admin.rotate(self.server, self.args_array2),
                         (True, "ErrorMsg"))

    def test_no_log_dir(self):

        """Function:  test_no_log_dir

        Description:  Test with no log directory passed.

        Arguments:

        """

        self.assertEqual(mongo_db_admin.rotate(self.server, self.args_array),
                         (False, None))


if __name__ == "__main__":
    unittest.main()
