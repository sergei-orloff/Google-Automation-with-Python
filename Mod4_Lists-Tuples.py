def skip_elements(elements):
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)

    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

# =====================================================================
"""With the given list of "filenames", this code should rename all files with the extension .hpp to the extension .h.
The code should then generate a new list called "new_filenames" that contains the file names with the new extension.
You are given a list of filenames like this:

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

Output the list with all the “.hpp” files renamed to “.h”. Leave the other filenames alone. For this question,
you must use a for loop to create the list."""

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filename = filename.replace(".hpp", ".h")
        new_filenames.append(new_filename)
    else:
        new_filenames.append(filename)

print(new_filenames)
# ---------------------------------------------
"""Same task using a list comprehension."""

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_filenames = [filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename for filename in filenames]

print(new_filenames)

# =================================================================

"""Create a function that turns text into pig latin. Pig latin is a simple text transformation that modifies each
word by:

moving the first character to the end of each word;

then appending the letters "ay" to the end of each word.

For example, python ends up as ythonpay."""


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        word = word[1:] + word[0] + "ay"
        say += word + " "
    # Turn the list back into a phrase
    return say.strip()


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

# =======================================================

""" The “biography_list” function reads in a list of tuples “people”, which contains the name, age, and profession of
each “person”. Then, prints the sentence "__ is _ years old and works as __.". For example, “biography_list([("Ira",
30, "a Chef")])” should print: “Ira is 30 years old and works as a Chef.”"""


def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples.
    for person in people:
        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"
        name, age, profession = person

        # Format the required sentence and place the 3 variables
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and works as {}".format(name, age, profession))


# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])

# =======================================================================
