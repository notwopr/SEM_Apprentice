import datetime as dt
import re

class TimeStamp:

    def __init__(self):
        self.__dtobj = dt.datetime.now()
    
    @property
    def dtobject(self):
        return self.__dtobj

    @property
    def string_justnums(self):
        return re.sub(r'\.|\:|\-|\s', '', str(self.__dtobj))