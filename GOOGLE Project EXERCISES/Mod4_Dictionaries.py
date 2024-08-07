"""calculate the sum of the values in a dictionary."""
"""This function returns the total time, with minutes represented as 
decimals (example: 1 hour 30 minutes = 1.5), for all end user time
spent accessing a server in a given day. """


def sum_server_use_time(Server):
    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items
    # using a for loop.
    for key, value in Server.items():
        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]

    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)


FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer))  # Should print 20.1

# ============================================

"""Skill Group 2 
* Concatenate a value, a string, and the key for each item in the dictionary and append to the end of 
a new list[ ] using the list.append(x) method.
* Iterate over keys with multiple values from a dictionary using nested for loops with the dictionary.items() method."""

"""This function receives a dictionary, which contains common employee 
last names as keys, and a list of employee first names as values. 
The function generates a new list that contains each employees’ full
name (First_name Last_Name). For example, the key "Garcia" with the 
values ["Maria", "Hugo", "Lucia"] should be converted to a list 
that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"]."""


def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.
    full_names = []

    # The outer for loop iterates through each "last_name" key and
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:
            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name".
            full_names.append(first_name + " " + last_name)

    # Return the new "full_names" list once the outer for loop has
    # completed all iterations.
    return full_names


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']

# =========================================================
"""Skill Group 3  
- Use the dictionary[key] = value operation to associate a value with a key in a dictionary.   
- Iterate over keys with multiple values from a dictionary, using nested for loops and an if-statement, 
and the dictionary.items() method.
- Use the dictionary[key].append(value) method to add the key, a string, and the key for each item in the dictionary."""
# ...........................
"""This function receives a dictionary, which contains resource 
categories (keys) with a list of available resources (values) for a 
company’s IT Department. The resources belong to multiple categories.
The function should reverse the keys and values to show which 
categories (values) each resource (key) belongs to. """


def invert_resource_dict(resource_dictionary):
    # Initialize a "new_dictionary" variable as a dict data type using
    # empty {} curly brackets.
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed
    # all iterations.
    return new_dictionary


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
                            "PC Parts": ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"],
                            "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video
# cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}

# ============================================

"""The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values."""


def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return emails


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]}))
# ===========================================================

"""The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can 
belong to multiple groups."""


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)

    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))
# ===========================================================

"""The add_prices function returns the total price of all of the groceries in the  dictionary."""


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for price in basket.values():
        # Add each price to the total calculation
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44
