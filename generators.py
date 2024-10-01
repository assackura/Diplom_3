import string
import random


class UserGenerator:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_email():
        letters = string.ascii_lowercase
        random_email = ''.join(random.choice(letters) for i in range(5))
        random_email += '@'
        random_email += ''.join(random.choice(letters) for i in range(5))
        random_email += '.'
        random_email += ''.join(random.choice(letters) for i in range(2))
        return random_email