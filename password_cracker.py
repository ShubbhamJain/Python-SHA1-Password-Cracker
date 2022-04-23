import hashlib


def crack_sha1_hash(hash, use_salts=False):
    answer = ""
    passwords = open("top-10000-passwords.txt", "r")

    for line in passwords:
        password = line.splitlines()[0]

        if use_salts == True:
            salts = open("known-salts.txt", "r")
            for salt in salts:
                salted = salt.splitlines()[0]
                encodedPassword = (salted + password).encode()
                hashedPassword = hashlib.sha1(encodedPassword).hexdigest()

                if hash == hashedPassword:
                    answer = password

                encodedPassword = (password + salted).encode()
                hashedPassword = hashlib.sha1(encodedPassword).hexdigest()

                if hash == hashedPassword:
                    answer = password

            salts.close()

        else:
            encodedPassword = password.encode()
            hashedPassword = hashlib.sha1(encodedPassword).hexdigest()

            if hash == hashedPassword:
                answer = password

    passwords.close()

    if len(answer) > 0:
        return answer

    return "PASSWORD NOT IN DATABASE"
