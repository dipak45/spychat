from datetime import datetime
default_password ="Dipak"
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('Dipak', 'Mr.', 20, 4.7)

friend_one = Spy('Manish', 'Mr.', 20, 5)
friend_two = Spy('Rekha', 'Mrs.', 19, 8)
friend_three = Spy('Dilshad', 'Mr', 21, 7)

friends = [friend_one, friend_two, friend_three]