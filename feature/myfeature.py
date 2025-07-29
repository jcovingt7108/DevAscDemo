import random
import string

def generate_strong_password(length=12):
    """Generate a strong random password."""
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated password:", generate_strong_password())
    print("welcome to DevAsco")
    print 
    final_password = generate_strong_password(16)