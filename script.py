import sys

print(sys.version)
print(sys.executable)

def greeting(who):
  return 'Hello, {}'.format(who)

print(greeting('Chief'))