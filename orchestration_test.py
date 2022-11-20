import unittest
from messages import DisplayNotification
from messages import PictureNotification
from orchestration import Orchestration

class TestSubscriber:
    def __init__(self) -> None:
        self.value = None
        self.source = None
        self.detination = None
        self.timestamp = None
    
    def process_picture_notifiaction(self, message: PictureNotification):
        self.value = message.image
        self.source = message.source
        self.detination = message.destination
        self.timestamp = message.timestamp
    
    def process_display_notifiacton(self, message: DisplayNotification):
        self.value = message.text
        self.source = message.source
        self.detination = message.destination
        self.timestamp = message.timestamp
        

class OrchestrationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_subsriber_1 = TestSubscriber()
        self.test_subsriber_2 = TestSubscriber()
        self.test_subsriber_3 = TestSubscriber()
        return super().setUp()

    def __compare_message_and_subscriber_display(self, msg: DisplayNotification, sub: TestSubscriber):
        self.assertEqual(msg.timestamp, sub.timestamp)
        self.assertEqual(msg.text, sub.value)
        self.assertEqual(msg.source, sub.source)
        self.assertEqual(msg.destination, sub.detination)

    def __compare_message_and_subscriber_picture(self, msg: PictureNotification, sub: TestSubscriber):
        self.assertEqual(msg.timestamp, sub.timestamp)
        self.assertEqual(msg.image, sub.value)
        self.assertEqual(msg.source, sub.source)
        self.assertEqual(msg.destination, sub.detination)

    def test_message_recieved(self):
        msg_type = DisplayNotification
        func = self.test_subsriber_1.process_display_notifiacton
        Orchestration.register(msg_type, func)
        msg = DisplayNotification(0,"test_message_recieved")
        
        Orchestration.send(msg)

        self.__compare_message_and_subscriber_display(msg, self.test_subsriber_1)

    def test_message_recieved_multiple_subsriber(self):
        msg_type = DisplayNotification
        func1 = self.test_subsriber_1.process_display_notifiacton
        func2 = self.test_subsriber_2.process_display_notifiacton
        Orchestration.register(msg_type, func1)
        Orchestration.register(msg_type, func2)
        msg = DisplayNotification(0,"test_message_recieved_multiple_subsriber")
        
        Orchestration.send(msg)

        self.__compare_message_and_subscriber_display(msg, self.test_subsriber_1)
        self.__compare_message_and_subscriber_display(msg, self.test_subsriber_2)

    def test_message_not_recieved_not_subscribed(self):
        msg_type = DisplayNotification
        func = self.test_subsriber_1.process_display_notifiacton
        Orchestration.register(msg_type, func)
        msg = DisplayNotification(0,"test_message_recieved")
        
        Orchestration.send(msg)

        self.__compare_message_and_subscriber_display(msg, self.test_subsriber_1)

        self.assertNotEqual(msg.timestamp, self.test_subsriber_2.timestamp)
        self.assertNotEqual(msg.text, self.test_subsriber_2.value)
        self.assertNotEqual(msg.source, self.test_subsriber_2.source)
        self.assertNotEqual(msg.destination, self.test_subsriber_2.detination)
        