import os
import subprocess

print(os.environ)

os.environ['PHASE'] = 'dev'

print(os.environ['PHASE'])
