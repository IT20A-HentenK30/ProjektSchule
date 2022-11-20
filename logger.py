from asyncio import Lock
from datetime import datetime
import platform
import os
import inspect

class LoggerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=LoggerMeta):
    
    PATH_WINDOWS: str       = "C:\\ProgramData\\Personenerkennung\\Logs\\"
    PATH_LINUX: str         = "/var/Personenerkennung/Logs/"
    FILE_FORMAT: str        = "%d_%m_%Y"
    TIME_FORMAT: str        = "[%H:%M:%S]"
    FILE_TYPE: str          = ".txt"
    LOGLEVEL_TRACE: str     = "[TRACE]"
    LOGLEVEL_DEBUG: str     = "[DEBUG]"
    LOGLEVEL_INFO: str      = "[INFO]"
    LOGLEVEL_WARNING: str   = "[WARNING]"
    LOGLEVEL_ERROR: str     = "[ERROR]"
    LOGLEVEL_FATAL: str     = "[FATAL]"

    def __init__(self) -> None:
        os_name = platform.system()
        if os_name == "Linux":
            self.log_dir = self.PATH_LINUX
        elif os_name == "Windows":
            self.log_dir = self.PATH_WINDOWS
        else: 
            raise Exception(f"Platform {os_name} not supported")
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        super()
    
    def trace(self, message):
        caller = inspect.getmodule(inspect.stack()[1][0]).__name__
        self._write_log(self.LOGLEVEL_TRACE, caller, message)
    
    def debug(self, message):
        caller = inspect.getmodule(inspect.stack()[1][0]).__name__
        self._write_log(self.LOGLEVEL_DEBUG, caller, message)
    
    def info(self, message):
        caller = inspect.getmodule(inspect.stack()[1][0]).__name__
        self._write_log(self.LOGLEVEL_INFO, caller, message)
    
    def warn(self, message):
        caller = inspect.getmodule(inspect.stack()[1][0]).__name__
        self._write_log(self.LOGLEVEL_WARNING, caller, message)
    
    def error(self, message):
        caller = inspect.getmodule(inspect.stack()[1][0]).__name__
        self._write_log(self.LOGLEVEL_ERROR, caller, message)
    
    def fatal(self, message):
        caller = inspect.getmodule(inspect.stack()[1][0]).__name__
        self._write_log(self.LOGLEVEL_FATAL, caller, message)

    def _write_log(self, loglevel, caller, message):
        file = self._open_logfile()
        time = datetime.now().strftime(self.TIME_FORMAT)
        log_entry = time + loglevel + "[" + caller + "]" + message
        file.writelines(log_entry + "\n")
        file.close()

    def _open_logfile(self):
        file_path = self.get_file_path()
        file = open(file_path, "a")
        return file

    def get_file_path(self) -> str:
        return self.log_dir + datetime.now().strftime(self.FILE_FORMAT) + self.FILE_TYPE 
    