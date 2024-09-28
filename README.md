
# Python Randomised Password Generator

A randomized password generator that encrypts the generated password and stores it in a file with a username as the key to the encrypted password. Made with Python.

## Features

- Generate a random password
- SHA256 Encryption
- Save user passwords to a file

## Usage

Entering an unused username with generate and store a password.
<br />
```
$python3 passgen.py
Enter username: testing 
Generated Password: '?^&y)cT#h('
Encrypted Password: 'a3eeca1f97ba6eec2ee2dd1d6c12262db0289b938e9b9c9fe986b3f2c2db5da5'
User password saved!
```

Entering an already existing user name will end the script.
<br />
```
$python3 passgen.py
Enter username: testing
Username already exists!
```
