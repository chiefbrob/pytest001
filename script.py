import sys
import requests

print(sys.version)
print(sys.executable)


def greeting(who):
    return 'Hello, {}'.format(who)


print(greeting('Chief'))

r = requests.get('https://chiefbrob.info')
print(r.status_code)
