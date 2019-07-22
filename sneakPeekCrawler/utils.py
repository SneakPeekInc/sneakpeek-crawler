import os

def isDevelopment():
    return os.environ['ENV'] == 'development'

def getBrands():
    return ['nike', 'newbalance']
