import random
import string


class Random_utils:

    @staticmethod
    def generate_first_name():
        return ''.join(random.choice(string.ascii_lowercase) for x in range(9))

    @staticmethod
    def generate_phone():
        return random.randint(1000000000, 9999999999)
