person = {'name': 'Jenn', 'age': 23}
person1 =["Jenn", 23]

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
# sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(person1)


# tag = 'h1'
# text = 'This is a headline'
# sentence = '<{0}>{1}</{0}>'.format(tag, text)


# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Jack', '33')
# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)


# print(sentence)


# for i in range(1, 11):
#     sentence = 'The value is {:02}'.format(i)
#     print(sentence)


# pi = 3.14159265
# sentence = 'Pi is equal to {:.3f}'.format(pi)


# sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)

# print(sentence)


import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

print(my_date)

# sentence = '{:%B %d, %Y}'.format(my_date)
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
