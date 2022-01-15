"""
This is examples of list and dict comprehensions.

i - enumerate index
value - enumerate value
"""


key = ['first', 'second']
value = [[1, 2], ['one', 'two']]

print({key[i]: value for i, value in enumerate(value)})  # {'first': [1, 2], 'second': ['one', 'two']}
print([{key[i]: value for i, value in enumerate(value)} for j in value])  #[{'first': 1, 'second': 2}, {'first': 'one', 'second': 'two'}]


