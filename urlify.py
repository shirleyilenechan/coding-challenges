# replace spaces in string with %20;
# string has additional space in the end to hold additional characters 


def urlify(string):
    new_string = string.rstrip().lstrip()
    new_string = new_string.split()
    new_string = "%20".join(new_string)
    return new_string
