from sys import argv

script, first_name, last_name = argv
prompt = "> "

print("Hi {} {}, I'm the {} script.".format(first_name, last_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me {} {}?".format(first_name, last_name))
likes = input(prompt)

print("Where do you live {} {}?".format(first_name, last_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(''' Alright, so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice.
'''.format(likes, lives, computer))
