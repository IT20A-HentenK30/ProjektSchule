from logger import Logger


class OrchestrationMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class Orchestration(metaclass=OrchestrationMeta):
    _subscriber: list = []
    
    def __init__(self) -> None:
        self._logger = Logger()

    def register(self, type: type, func):
        Orchestration._subscriber.append((type, func))
        
    def send(self, message):
        for msg in Orchestration._subscriber:
            if type(message) is msg[0]:
                try:
                    msg[1](message)
                except:
                    self._logger.error(f"Fuction could not be called. [type:{msg[0]}][function:{msg[1]}]")
