import logging
import coloredlogs
import verboselogs

FMT = "%(asctime)s %(levelname)-10s %(name)-12s %(lineno)-4d %(processName)-12s   %(message)s"


def _fmt_filter(record: logging.LogRecord):
    record.levelname = "[%s]" % record.levelname
    record.funcName = "[%s]" % record.funcName
    return True


def get_logger(name: str) -> verboselogs.VerboseLogger:
    logger = verboselogs.VerboseLogger(name)
    logger.setLevel(logging.SPAM)
    # formatter = logging.Formatter(FMT)
    # handler = logging.StreamHandler()
    # handler.setFormatter(formatter)
    # logger.addFilter(_fmt_filter)
    coloredlogs.install(
        level=logging.SPAM,
        fmt="%(asctime)s:%(msecs)03d %(levelname)-10s %(name)-18s %(lineno)-4d %(processName)-12s   %(message)s",
        datefmt="%H:%M:%S",
    )
    return logger


logging.basicConfig(level=verboselogs.SPAM)
