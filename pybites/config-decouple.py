from decouple import config, Csv

my_value = config('MY_VALUE')
debug = config('DEBUG', default=False, cast=bool)
list_of_values = config('LIST_OF_VALUES', cast=Csv())

print (f"MY_VALUE = {my_value}")
print (f"DEBUG = {debug}")
print (f"CSV = {list_of_values}")

for val in list_of_values:
    print (f'Field = {val}')
