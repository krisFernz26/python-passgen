import string
import random
import hashlib
import os
import json
import stat
import errno
from pathlib import Path

# Current Working Directory
save_path = Path.cwd()
name_of_file = "users.json"
complete_name = os.path.join(save_path, name_of_file)

length: int = 10

### Generate Randomized Password
def generate_password():
    # Get current users from file
    password_dict = get_users()

    # Input username who owns the password
    username = input("Enter username: ")

    # Check if username already has password stored
    # Exit function if it already exists
    if username in password_dict.keys():
        print("Username already exists!")
        return

    # Generate random characters
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Randomise character placement
    password = ''.join(random.choice(alphabet) for i in range(length))
    print("Generated Password: '%s'" % (password))

    # Encrypt generated randomised passwords
    encrypted_password = encrypt_password(password)

    # Store generated password to a dictionary
    password_dict[username] = encrypted_password
    # Save the dictionary to the file
    save_file(password_dict)

### Encrypt a password using SHA256
def encrypt_password(password: str):
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    print("Encrypted Password: '%s'" % (encrypted_password))
    return encrypted_password

### Save the dictionary to users file
def save_file(password_dict: dict):
    users_file = open(complete_name, 'w')
    users_file.write(json.dumps(password_dict))
    users_file.close()
    print("User password saved!")

### Get the users from the users file
def get_users():
    # Return an empty dictionary if file does not exist
    if not os.path.exists(complete_name):
        create_file()
        return {}
    # Check if current user has appropriate permissions
    try:
        open(complete_name).close()
    except IOError as err:
        if err.errno == errno.EACCES:
            raise Exception(err)
    users_file = open(complete_name, 'r')
    password_dict = json.loads(users_file.read())
    users_file.close()
    return password_dict

### Create the users file if it doesn't exist
def create_file():
    users_file = open(complete_name, 'w').close()
    # Change file permisions to allow only the owner to read, write, and execute the file.
    os.chmod(complete_name, stat.S_IRWXU)

generate_password()
