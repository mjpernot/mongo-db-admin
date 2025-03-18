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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_admin                           # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

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

        return arg in self.args_array

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Server():                                         # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        adm_cmd

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None
        self.server_status = {"version": "7.0.16"}
        self.arg1 = None

    def adm_cmd(self, cmd, arg1=None):

        """Method:  adm_cmd

        Description:  Stub holder for mongo_class.Server.adm_cmd method.

        Arguments:
            (input) cmd -> Database command.

        """

        status = "Command completed"
        self.arg1 = arg1

        if cmd == "serverStatus":
            return self.server_status

        return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_pre_500
        test_post_500
        test_compress
        test_too_many_logs
        test_rotate
        test_file_chk_fail
        test_no_log_dir

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {}
        self.args2.args_array = {"-n": "/path"}
        self.args3.args_array = {"-n": "/path", "-p": True}
        self.filepath = "/dir/path/filename"
        self.results = (True, None)
        self.results2 = (
            False, "Error:  Too many files to move: ['File1', 'File2']")
        self.results3 = (False, "ErrorMsg")

    @mock.patch("mongo_db_admin.gen_libs.is_missing_lists")
    @mock.patch("mongo_db_admin.gen_libs.mv_file")
    @mock.patch("mongo_db_admin.gen_libs.dir_file_match")
    @mock.patch("mongo_db_admin.mongo_class.fetch_cmd_line")
    @mock.patch("mongo_db_admin.gen_libs.chk_crt_dir")
    def test_pre_500(                                   # pylint:disable=R0913
            self, mock_check, mock_fetch, mock_match, mock_mv, mock_diff):

        """Function:  test_pre_500

        Description:  Test with Mongo version before 5.0.0.

        Arguments:

        """

        self.server.server_status = {"version": "4.2.29"}

        mock_check.return_value = (True, None)
        mock_fetch.return_value = {
            "parsed": {"systemLog": {"path": self.filepath}}}
        mock_match.side_effect = [["File1", "File2"], ["File1", "File2"]]
        mock_mv.return_value = True
        mock_diff.return_value = ["File1"]

        self.assertEqual(
            mongo_db_admin.rotate(self.server, self.args2), self.results)

    @mock.patch("mongo_db_admin.gen_libs.is_missing_lists")
    @mock.patch("mongo_db_admin.gen_libs.mv_file")
    @mock.patch("mongo_db_admin.gen_libs.dir_file_match")
    @mock.patch("mongo_db_admin.mongo_class.fetch_cmd_line")
    @mock.patch("mongo_db_admin.gen_libs.chk_crt_dir")
    def test_post_500(                                  # pylint:disable=R0913
            self, mock_check, mock_fetch, mock_match, mock_mv, mock_diff):

        """Function:  test_post_500

        Description:  Test with Mongo version greater than 5.0.0.

        Arguments:

        """

        mock_check.return_value = (True, None)
        mock_fetch.return_value = {
            "parsed": {"systemLog": {"path": self.filepath}}}
        mock_match.side_effect = [["File1", "File2"], ["File1", "File2"]]
        mock_mv.return_value = True
        mock_diff.return_value = ["File1"]

        self.assertEqual(
            mongo_db_admin.rotate(self.server, self.args2), self.results)

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
        mock_fetch.return_value = {
            "parsed": {"systemLog": {"path": self.filepath}}}

        self.assertEqual(
            mongo_db_admin.rotate(self.server, self.args3), self.results)

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

        mock_check.return_value = (True, None)
        mock_fetch.return_value = {
            "parsed": {"systemLog": {"path": self.filepath}}}
        mock_match.side_effect = [["File1", "File2"], ["File1"]]
        mock_diff.return_value = ["File1", "File2"]

        self.assertEqual(
            mongo_db_admin.rotate(self.server, self.args2), self.results2)

    @mock.patch("mongo_db_admin.gen_libs.is_missing_lists")
    @mock.patch("mongo_db_admin.gen_libs.mv_file")
    @mock.patch("mongo_db_admin.gen_libs.dir_file_match")
    @mock.patch("mongo_db_admin.mongo_class.fetch_cmd_line")
    @mock.patch("mongo_db_admin.gen_libs.chk_crt_dir")
    def test_rotate(                                    # pylint:disable=R0913
            self, mock_check, mock_fetch, mock_match, mock_mv, mock_diff):

        """Function:  test_rotate

        Description:  Test rotate function.

        Arguments:

        """

        mock_check.return_value = (True, None)
        mock_fetch.return_value = {
            "parsed": {"systemLog": {"path": self.filepath}}}
        mock_match.side_effect = [["File1", "File2"], ["File1", "File2"]]
        mock_mv.return_value = True
        mock_diff.return_value = ["File1"]

        self.assertEqual(
            mongo_db_admin.rotate(self.server, self.args2), self.results)

    @mock.patch("mongo_db_admin.gen_libs.chk_crt_dir")
    def test_file_chk_fail(self, mock_check):

        """Function:  test_file_chk_fail

        Description:  Test with file checking fails.

        Arguments:

        """

        mock_check.return_value = (False, "ErrorMsg")

        self.assertEqual(
            mongo_db_admin.rotate(self.server, self.args2), self.results3)

    def test_no_log_dir(self):

        """Function:  test_no_log_dir

        Description:  Test with no log directory passed.

        Arguments:

        """

        self.assertEqual(
            mongo_db_admin.rotate(self.server, self.args), self.results)


if __name__ == "__main__":
    unittest.main()
