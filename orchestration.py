class Orchestration:
    _subscriber: list = []

    def register(type: type, func):
        Orchestration._subscriber.append((type, func))
        
    def send(message):
        for msg in Orchestration._subscriber:
            if type(message) is msg[0]:
                try:
                    msg[1](message)
                except:
                    pass
