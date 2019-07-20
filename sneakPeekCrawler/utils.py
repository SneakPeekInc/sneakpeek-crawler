import os

def isDevelopment():
    return os.environ['ENV'] == 'development'

def brandsInfo():
    return ['nike', 'newbalance']
