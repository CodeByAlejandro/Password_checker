from getpass import getpass
from pathlib import Path
from hashlib import sha1
import sys

import requests


def request_pwned_api_data(query_str):
    url = "https://api.pwnedpasswords.com/range/" + query_str
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the API and try again"
        )
    return res


def check_against_pwned_api(password):
    sha1_pass = sha1(password.encode('UTF-8')).hexdigest()
    sha1_pass_prefix, sha1_pass_suffix = sha1_pass[:5], sha1_pass[5:]
    data = request_pwned_api_data(sha1_pass_prefix.upper())
    nbr_of_leaks = 0
    hash_data = (hashline.split(':') for hashline in data.text.splitlines())
    # Catch any extra attr in 'dummy' for compatibility with future changes
    for sha1_suffix, occurrences, *dummy in hash_data:
        if sha1_suffix.upper() == sha1_pass_suffix.upper():
            nbr_of_leaks = occurrences
            break
    return nbr_of_leaks


def check_password_safety(password):
    leaks = check_against_pwned_api(password)
    if leaks != 0:
        print(
            f"Password {'*' * len(password)} was found {leaks} times... " +
            "You should probably change it!"
        )
    else:
        print(f"Password {'*' * len(password)} was NOT found. Carry on!")


def main(args):
    if len(args) < 2:
        password = getpass()
        check_password_safety(password)
    elif len(args) == 2:
        pass_file_path = Path(args[1])
        if pass_file_path.is_file():
            with open(pass_file_path, 'rt') as pass_file:
                for line in pass_file:
                    password = line.rstrip()
                    check_password_safety(password)
        else:
            check_password_safety(args[1])
    else:
        for password in args[1:]:
            check_password_safety(password)


if __name__ == "__main__":
    main(sys.argv)
