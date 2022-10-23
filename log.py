import datetime as dt


def writeLog(logMsg):
    date = dt.date


    log = open("logs/log.txt", "a")
    log.write(date + " " + logMsg)
    log.close()