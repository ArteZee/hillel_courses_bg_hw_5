# Enter your object
method_python_object: str = input("Enter python object: \n ")

if method_python_object == "set":
    x = set
elif method_python_object == "str":
    x = str
elif method_python_object == "dict":
    x = dict
elif method_python_object == "tuple":
    x = tuple
elif method_python_object == "list":
    x = []

lst_of_all_dir = dir(x)
# create new list for methods of object
lst_of_method_dir = []

for i in lst_of_all_dir:
    if "_" in i:
        continue
    else:
        lst_of_method_dir.append(i)

print(lst_of_method_dir)
