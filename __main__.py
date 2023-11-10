from general.config import get_config
from general.logger import init_logger
from logging import getLogger
import pyray as pr
from constants import WIDTH, HEIGHT
from engine import render

config = get_config()
init_logger(config.LOG_LEVEL, config.LOG_FILE, config.CONSOLE_ENABLED)
logger = getLogger(__name__)

def main():
    pr.init_window(WIDTH, HEIGHT, "Hello Pyray")
    pr.set_target_fps(60)

    while not pr.window_should_close():
        render()
    pr.close_window()


if __name__ == "__main__":
    main()