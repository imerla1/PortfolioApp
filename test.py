from werkzeug.security import generate_password_hash, check_password_hash

password = generate_password_hash('imerla')

print(check_password_hash(password, 'imerla'))