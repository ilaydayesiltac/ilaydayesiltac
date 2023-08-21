import random
import re
import string


class Tools:
    @staticmethod
    def is_valid_url(original_url):
        regex = ("((http|https)://)(www.)?" +
                 "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                 "{2,256}\\.[a-z]" +
                 "{2,6}\\b([-a-zA-Z0-9@:%" +
                 "._\\+~#?&//=]*)")

        p = re.compile(regex)

        if original_url is None or not re.search(p, original_url):
            return False

        return True

    @staticmethod
    def generate_random_key(length):
        characters = string.ascii_letters + string.digits
        random_key = ''.join(random.choice(characters) for _ in range(length))
        return random_key
