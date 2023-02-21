import secrets
import string

# secure random string
secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(12)))
print(secure_str)

# secure password
password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(12)))
print(password)