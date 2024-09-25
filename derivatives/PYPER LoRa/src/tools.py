import time
import sys
import settings

def log_exc(exc:Exception, msg:str = None) -> None:
    f = open("log.txt", "a")
    f.write("--- EXCEPTION at " + str(time.ticks_ms()) + " ms ---" + "\n")
    if msg != None: # if they provided an optional msg, append it after
        f.write("Developer Msg: " + msg)
        f.write("\n")
    sys.print_exception(exc, f)
    f.write("\n")
    f.close()

def log(text:str) -> None:
    print(text)
    if settings.dlog: # only log if diagnostic logging is turned on in settings
        f = open("log.txt", "a")
        f.write("Log @ " + str(time.ticks_ms())  + " ms: " + text)
        f.write("\n")
        f.close()