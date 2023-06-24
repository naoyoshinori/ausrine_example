import config
import time

from ausrine import Ausrine
from ausrine.chrome import setup_webdriver
from logging import getLogger
from logging_support import initialize_simple_logger

logger = getLogger("main")


def setup():
    logger.debug("setup")
    initialize_simple_logger(name="main", level=config.logging_level)
    initialize_simple_logger(name="ausrine", level=config.logging_level)


def cleanup():
    logger.debug("cleanup")


def main():
    logger.debug("main start")

    webdriver = setup_webdriver(
        user_data_dir=config.user_data_dir,
        profile_dir=config.profile_dir,
        download_dir=config.download_dir,
    )

    ausrine = Ausrine(webdriver)
    ausrine.execute(config.sequences)
    time.sleep(5)

    logger.debug("main end")


if __name__ == "__main__":
    setup()
    main()
    cleanup()
