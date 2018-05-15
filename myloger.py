import logging
import pathlib

class MyLogging:
    FILE_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    STDOUT_FORMAT = '%(asctime)s %(message)s'

    def __init__(self, logfile, flag=None,level=logging.DEBUG):
        logging.basicConfig(level=level,
                            forma=self.STDOUT_FORMAT,
                            datefmt='%Y:%m:%d %H:%M:%S'
                            )
        self.level_dict = {'debug': self.logger.debug, 'info': self.logger.info, 'warning': self.logger.warning,
                      'error': self.logger.error, 'critical': self.logger.critical}
        self.level = level
        self.path = logfile
        self.logger = logging.getLogger(flag)
        self.f_formatter = logging.Formatter(self.FILE_FORMAT)
        self.s_formatter = logging.Formatter(self.STDOUT_FORMAT)
        logfile = pathlib.Path(self.path)
        if not logfile.parent:
            pathlib.Path(logfile.parent).mkdir(parents=True)
        self.f_handler = logging.FileHandler(logfile)

    def log2file(self,level,msg):
        self.logger.addHandler(self.f_handler)
        self.f_handler.setFormatter(self.f_formatter)
        self.f_handler.setLevel(self.level)
        self.level_dict.get(level,lambda x: 0)(msg)

