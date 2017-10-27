from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_$l*dwz%)f7nv)6behbdfd*wh$x^g&5(=&@2o=%%fiykcqd-ne'

DEBUG = env.bool('DJANGO_DEBUG', default=True)