import time
import logging
from hotreload import Loader


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    script = Loader("scratchpad.py")

    while True:
        if script.has_changed():
            script.main()

        time.sleep(1)
