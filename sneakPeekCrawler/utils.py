import os

def isDevelopment():
    return os.environ['ENV'] == 'development'

