import hashlib

# Dummy database of users (replace this with a real database)
users = {
    'Sweshik': {
        'password': '2206',  # Password should be hashed in real scenarios
        'balance': 1000
    },
    'user2': {
        'password': 'password2',
        'balance': 2000
    }
}

def hash_password(password):
    """
    Hashes the given password using SHA-256 algorithm.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    """
    Authenticates the user with the given username and password.
    Returns True if authentication succeeds, False otherwise.
    """
    if username in users and users[username]['password'] == password:
        return True
    else:
        return False

# Example usage:
username = input("Enter your username: ")
password = input("Enter your password: ")

if authenticate(username, password):
    print("Authentication successful!")
    # Proceed with further operations
else:
    print("Authentication failed. Please check your username and password.")
