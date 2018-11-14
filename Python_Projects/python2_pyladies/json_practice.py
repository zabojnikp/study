import os
import json
os.path.dirname(os.path.realpath(__file__))

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], ensure_ascii=False))