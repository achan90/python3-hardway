name = 'Zed A. Shaw'
age = 35
height = 74  # Inches
height_si = height * 2.54  # Centimeters
weight = 180  # lbs
weight_si = weight * 0.453592  # Kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about {}.".format(name))
print("He's {} inches or {} centimeters tall.".format(height, height_si))
print("He's {} pounds or {} kilograms heavy.".format(weight, weight_si))
print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.".format(eyes, hair))
print("His teeth are usually {} depending on the coffee.".format(teeth))

print("If I add {}, {} and {} I get {}.".format(
    age, height, weight, age + height + weight))
