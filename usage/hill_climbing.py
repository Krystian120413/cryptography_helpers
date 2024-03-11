import random
import time
from ngram_score import NgramScore
import textwrap
from encrypt import encrypt, decrypt
from consts import alphabet
from samples import mint_water

ns = NgramScore("./../english_bigrams.txt")


def change_key1(key: str) -> str:
    key = list(key)
    r1, r2 = random.sample(list(range(len(key))), 2)
    (key[r1], key[r2]) = (key[r2], key[r1])

    return "".join(key)


def twist2(key: str):
    key = list(key)
    r1, r2 = sorted(random.sample(list(range(len(key))), 2))
    new_key = key[:r1] + [key[r2]] + key[r1 + 1: r2] + [key[r1]] + key[r2 + 1:]

    return "".join(new_key)


def change_key(key: str) -> str:
    r: float = random.random()
    new_key = ''
    if r < 0.9:
        new_key = change_key1(key)
    elif r < 0.95:
        new_key = twist2(key)

    return new_key


def hill_climbing(encrypted_text, timelimit: int = 20):
    old_key = "".join(random.sample(list(alphabet), len(alphabet)))
    old_score = ns.score(decrypt(encrypted_text, old_key))
    t1 = time.time()
    print("Climbing...")

    while time.time() - t1 < timelimit:
        new_key = change_key(old_key)
        new_score = ns.score(decrypt(encrypted_text, new_key))
        if new_score > old_score:
            old_key = new_key
            old_score = new_score
            print(f'old_score = {old_score}')

    return [old_score, old_key, decrypt(encrypted_text, old_key)]


if __name__ == '__main__':
    sample_text = mint_water
    encryption_key = 'ABCDMNOPQEFGHIJXYKLRSTUVWZ'
    encrypted_text = encrypt(sample_text, encryption_key)

    print(textwrap.fill(encrypted_text, 100))

    score, key, decrypted_text = hill_climbing(encrypted_text)

    print(f"Score: {score}")
    print(f"Key: {key}")
    print(textwrap.fill(decrypted_text, 100))
