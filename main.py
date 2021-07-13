import logging

from services.custom_loging import get_logger


logger = get_logger(filename="events_log.json", level=logging.INFO)


def main():
    events = [{"x": "x_0", "y": "y_0"}, {"x": "x_1", "y": "y_1"}]
    logger.info("my-events", extra={"events": events})


if __name__ == "__main__":
    main()

