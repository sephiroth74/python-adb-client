import logging
import coloredlogs
import verboselogs

from pythonadb import set_logging_factory

FMT = "%(asctime)s %(levelname)-10s %(name)-12s %(lineno)-4d %(processName)-12s   %(message)s"


def _fmt_filter(record: logging.LogRecord):
    record.levelname = "[%s]" % record.levelname
    record.funcName = "[%s]" % record.funcName
    return True


def get_logger(name: str) -> verboselogs.VerboseLogger:
    verboselogs.install()
    logger = verboselogs.VerboseLogger(name)
    logger.setLevel(logging.SPAM)

    coloredlogs.install(
        level=logging.SPAM,
        fmt="%(asctime)s:%(msecs)03d %(levelname)-10s %(name)-18s %(lineno)-4d %(processName)-12s   %(message)s",
        datefmt="%H:%M:%S",
        logger=logger
    )

    return logger


set_logging_factory(get_logger)

