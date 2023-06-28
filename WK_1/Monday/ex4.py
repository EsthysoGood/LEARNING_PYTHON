# Exercise Variables and Names
#this is an integer
cars = 100
#this is a floating point number
space_in_a_car = 4.0
#used the underscore character 
drivers = 30
#variables and an assigned value
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")
