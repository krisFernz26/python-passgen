
# Python Randomised Password Generator

A basic randomized password generator that encrypts the generated password and stores it in a file with a username as the key to the encrypted password. Made with Python.

## Features

- Generate a random password
- SHA256 Encryption
- Save user passwords to a file
- File permissions

## Usage

Entering an unused username with generate and store a password.
<br />
```console
$python3 passgen.py
Enter username: testing 
Generated Password: '?^&y)cT#h('
Encrypted Password: 'a3eeca1f97ba6eec2ee2dd1d6c12262db0289b938e9b9c9fe986b3f2c2db5da5'
User password saved!
```

Entering an already existing user name will end the script.
<br />
```console
$python3 passgen.py
Enter username: testing
Username already exists!
```

users.json
<br />
```
{
	"testing": "1ce924ee13f8f1c7bd8516d546cc45212069a578733f96e81a05885f0f2744fc", 
	"testing1": "f9e227d8dcc3d1de75e4d29184777a98e98efa44846ce89189bfb2635e7c85eb", 
	"testing2": "e5683f05bc7c502a7000b935c6f5e4785d49e25be06b964fd6a03af57631426e"
}
```
