import itertools

def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    word_generator = (word for word in sentence.split())
    st = ''
    for i in word_generator:
        st += words[i] + ' '
    return st

print(translate("el gato esta en la casa"))


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    return next((a for a in itertools.count(n + 1) if is_prime(a)))

print(first_prime_over(1000000))