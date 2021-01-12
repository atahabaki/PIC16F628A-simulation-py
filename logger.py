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

    def __init__(self, name="Logger"):
        self.name=name

    def debug(self,topic,msg):
        print(f"[D] {self.name}:{topic}: ${msg}")

    def info(self,topic,msg):
        print(f"[I] {self.name}:{topic}: ${msg}")

    def warn(self,topic,msg):
        print(f"[W] {self.name}:{topic}: ${msg}")
