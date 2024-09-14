import time

def log_error(msg:str) -> None:
    f = open("log.txt", "a")
    f.write("--- ERROR at " + str(time.ticks_ms()) + " ms ---" + "\n")
    f.write(msg + "\n\n")
    f.close()