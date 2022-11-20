import unittest
from logger import Logger
from datetime import datetime
from os.path import exists

class LoggerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._logger = Logger()
        return super().setUp()
 
    def __get_latest_logentry(self) -> str:
        file_path = self._logger.get_file_path()
        with open(file_path, "r") as file:
            for line in file:
                pass
            last_line = line
            return last_line

    def test_can_write_trace(self):
        self._logger.trace("test_can_write_trace")
        last_log_entry = self.__get_latest_logentry()
        self.assertTrue(self._logger.LOGLEVEL_TRACE in last_log_entry)
    
    def test_can_write_debug(self):
        self._logger.debug("test_can_write_debug")
        last_log_entry = self.__get_latest_logentry()
        self.assertTrue(self._logger.LOGLEVEL_DEBUG in last_log_entry)
    
    def test_can_write_info(self):
        self._logger.info("test_can_write_info")
        last_log_entry = self.__get_latest_logentry()
        self.assertTrue(self._logger.LOGLEVEL_INFO in last_log_entry)
    
    def test_can_write_warning(self):
        self._logger.warn("test_can_write_warning")
        last_log_entry = self.__get_latest_logentry()
        self.assertTrue(self._logger.LOGLEVEL_WARNING in last_log_entry)
    
    def test_can_write_error(self):
        self._logger.error("test_can_write_error")
        last_log_entry = self.__get_latest_logentry()
        self.assertTrue(self._logger.LOGLEVEL_ERROR in last_log_entry)
    
    def test_can_write_fatal(self):
        self._logger.fatal("test_can_write_fatal")
        last_log_entry = self.__get_latest_logentry()
        self.assertTrue(self._logger.LOGLEVEL_FATAL in last_log_entry)
    
    def test_has_wright_entry_format(self):
        self._logger.info("test_has_wright_entry_format")
        time = datetime.now().strftime(self._logger.TIME_FORMAT)
        last_log_entry = self.__get_latest_logentry()
        self.assertTrue(time in last_log_entry)
    
    def test_has_wright_filename(self):
        self._logger.info("test_has_wright_filename")
        file_path = self._logger.get_file_path()
        self.assertTrue(exists(file_path))

    def test_logger_is_singleton(self):
        logger1 = Logger()
        logger2 = Logger()
        self.assertTrue(logger1 is logger2)
