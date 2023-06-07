from decouple import config

passw=config("pass")
user=config("user")
print(passw)
print(user)