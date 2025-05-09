import unittest
from src.main import ChatApp

class TestChatApp(unittest.TestCase):
    def setUp(self):
        self.chat_app = ChatApp()

    def test_respond(self):
        message = "こんにちは"
        chat_history = []
        response, new_chat_history = self.chat_app.respond(message, chat_history)
        self.assertIn(response, self.chat_app.acknowledgements)
        self.assertEqual(len(new_chat_history), 1)
        self.assertEqual(new_chat_history[0][0], message)
        self.assertIn(new_chat_history[0][1], self.chat_app.acknowledgements)

if __name__ == '__main__':
    unittest.main()
