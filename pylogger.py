import time
LOGFILEPREFIX = 'reddit'
LOGFILENAME = time.strftime("%Y%m%d")
bPrintToScreen = True


def add(KEY, DESC):
        f = open(LOGFILEPREFIX + '-' + LOGFILENAME + '.log', 'a')
        LOGSTRING = ''
        LOGSTRING = time.strftime("%Y%m%d,%H%M%S")
        LOGSTRING = LOGSTRING + ', ' + KEY.rstrip()
        LOGSTRING = LOGSTRING + ', ' + DESC.rstrip() + "\n"
        f.write(LOGSTRING)
        f.close()
        if bPrintToScreen:
            print(str("Logged: " + LOGSTRING).strip())