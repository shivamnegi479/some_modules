import os
from decouple import config  
...
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
passw=config("PASSWORD")
print(passw)
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)
TEMPLATE_DEBUG = config('TEMPLATE_DEBUG', cast=bool)
print(SECRET_KEY)