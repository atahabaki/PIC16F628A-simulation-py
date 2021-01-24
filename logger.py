from datetime import datetime as dt

class Logger:
    """
    A helper class which just logs...

    Attributes
    ----------

    name: str
        Name of the application which is using the Logger.

    Methods
    -------

    debug(topic=string,msg=string)
        Prints debug message at given topic.

    info(topic=string,msg=string)
        Prints info message at given topic.

    warn(topic=string,msg=string)
        Prints warn message at given topic.
    """

    def __init__(self, name="Logger", level=0):
        self.name=name
        self.level=level

    def __get_current_time(self):
        return dt.now().strftime("%H:%M:%S")

    def fatal(self,topic,msg):
        if self.level >= 0:
            print(f"[F] [{self.__get_current_time()}] {self.name}:{topic}: {msg}")

    def info(self,topic,msg):
        if self.level >= 1:
            print(f"[I] [{self.__get_current_time()}] {self.name}:{topic}: {msg}")

    def debug(self,topic,msg):
        if self.level >= 2:
            print(f"[D] [{self.__get_current_time()}] {self.name}:{topic}: {msg}")

    def warn(self,topic,msg):
        if self.level >= 3:
            print(f"[W] [{self.__get_current_time()}] {self.name}:{topic}: {msg}")
