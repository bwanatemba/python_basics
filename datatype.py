

# storing single values in a variable
number = 100  # Datatype- integer
second = 56.78  # Datatype- float
text = "Hello There"  # Datatype- string
ispythoninteresting = True  # Datatype- boolean

# storing multiple values in a variable
cars = ["toyota", "nissan", "mazda"]  # Datatype- List
fruits = ("banana", "orange", "apple") # Datatype- Tuple (values are Ordered and Unchangable)
countries = {"Kenya", "Uganda", "Tanzania"} # Datatype- Set

details= {                       # Datatype- Dictionary
    "firstname" : "Anada",
    "age" : 34,
    "course" : "Web Development",
    "nationality" : "Kenyan"
}

# Outputs
print(second)
print (text)
print(cars)
print(countries)
print(details ["firstname"],)
print(details ["age"],)
print(fruits)

# Determine the datatype of a Variable
#print(type(variable name))
print(type(text))
print(type(countries))
print(type(details))

# Typecasting- converting one datatype to another
print(float(number))
print(int(second))
