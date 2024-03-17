# Password_checker
Created python password checker that uses https://haveibeenpwned.com/. It accepts passwords via interactive input or via a password file given as cmd line argument or directly via cmd line arguments (not recommended).

# Installation
Install in virtual environment using following commands:
```shell
git clone https://github.com/CodeByAlejandro/Password_checker.git
cd Password_checker
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```
# Usage
There are 3 possible usages of this program:
1. Omit any cmd line arguments for interactive mode, which will safely request a password to check via cmd line input
2. Pass a passwordfile with multiple passwords to check
3. Pass one or more passwords directly on the cmd line (not recommended)

## Examples
```shell
python checkmypass.py
```
```shell
python checkmypass.py passwords.txt
```
```shell
python checkmypass.py P@ssw0rd qwerty123 hello
```

# Uninstall
Deactivate the virtual environment using the exported shell function `deactivate`:
```shell
deactivate
```
Remove the project:
```shell
cd ..
rm -rf Password_checker
```
