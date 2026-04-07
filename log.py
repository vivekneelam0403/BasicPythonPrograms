import time

def log(*arguments):
    print("-->      ", time.strftime("%H:%M"), " ",  *arguments)

log("Vivek,", "Logged In")


