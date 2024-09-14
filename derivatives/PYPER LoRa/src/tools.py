import time
import sys

def log_exc(exc:Exception) -> None:
    f = open("log.txt", "a")
    f.write("--- EXCEPTION at " + str(time.ticks_ms()) + " ms ---" + "\n")
    sys.print_exception(exc, f)
    f.write("\n")
    f.close()