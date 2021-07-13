from datetime import datetime
import json
import logging
import sys

import json_logging


def iso_time_format(datetime_):
    return "%04d-%02d-%02dT%02d:%02d:%02d.%03dZ" % (
        datetime_.year,
        datetime_.month,
        datetime_.day,
        datetime_.hour,
        datetime_.minute,
        datetime_.second,
        int(datetime_.microsecond / 1000),
    )


class CustomJSONLog(json_logging.JSONLogFormatter):
    """
    Customized logger
    """

    def format(self, record):
        utcnow = datetime.utcnow()

        json_customized_log_object = {
            "timestamp": iso_time_format(utcnow),
            "message": record.getMessage(),
        }

        if hasattr(record, "events"):
            json_customized_log_object['events'] = record.events

        return json.dumps(json_customized_log_object)


def get_logger(filename=None, level=logging.DEBUG):
    json_logging.init_non_web(custom_formatter=CustomJSONLog, enable_json=True)
    logger = logging.getLogger()
    logger.setLevel(level)
    handler_stdout = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler_stdout)
    if filename:
        handler_file = logging.FileHandler(filename)
        logger.addHandler(handler_file)
    return logger
