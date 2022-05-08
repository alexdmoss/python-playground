import random, string
from logger import log

password_length = 20

'''Other constants:
    string.ascii_letters
    string.ascii_lowercase
    string.ascii_uppercase
    string.digits
    string.hexdigits
    string.printable            # this is not as good as it sounds
    string.punctuation
'''

characters = string.ascii_letters + string.digits + string.punctuation

def gimme_a_password_with_sample():
    return ''.join(random.sample(characters, 20))

log.info("Random strings using sample")
for _ in range(5):
    print(gimme_a_password_with_sample())
