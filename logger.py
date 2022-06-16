import datetime
def Write(data):
    logFile = open('logs.csv', 'a')
    writeStr = f"""{datetime.datetime.now().strftime("%H:%M:%S")};{data}\n"""
    logFile.write(writeStr)
    logFile.close()
    return