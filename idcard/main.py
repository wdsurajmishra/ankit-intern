from data import data


def display_id(id):
    """
    Function to display the ID of the user.
    """

    for user in data:
        if user["id"]==id:
            print(f"Id Of {user['name']}")
                
    return None

print("Welcome to the User Information System")
userinput = int(input("Please enter the ID of the user you want to display: "))

output =  display_id(userinput);

