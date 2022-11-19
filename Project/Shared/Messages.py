

from abc import ABC
from datetime import datetime


class Message(ABC):

    DEST_SERVER: int = 0
    DEST_CLIENT_ALL: int = -1

    def __init__(self, destination):
        self._source = -99
        self._destination = destination
        self._timestamp = datetime.now()

    @property
    def source(self) -> int:
        return self._source

    @property
    def destination(self) -> int:
        return self._destination
    
    @property
    def timestamp(self) -> int:
        return self._timestamp
        

class PictureNotification(Message):

    def __init__(self, destination, image):
        self._image = image
        super().__init__(destination)

    @property
    def image(self):
        return self._image

class DisplayNotification(Message):

    def __init__(self, destination, text):
        self._text = text
        super().__init__(destination)

    @property
    def text(self):
        return self._text
    
