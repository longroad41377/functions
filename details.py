def get_information():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    gender = input("Enter gender: ")
    housenumber = input("Enter house number: ")
    street = input("Enter street: ")
    town = input("Enter town: ")
    postcode = input("Enter post code: ")
    return firstname, lastname, gender, housenumber, street, town, postcode

def welcome_message(firstname, lastname):
    print("Welcome {0} {1}".format(firstname, lastname))
    
firstname, lastname, gender, housenumber, street, town, postcode = get_information()

welcome_message(firstname, lastname)
