calculation_to_units = 24
name_of_unit = "hours"
user_input = "num_of_days"


def days_to_units(num_of_days):
  if num_of_days > 0:
    return(f"{num_of_days} days are {num_of_days * calculation_to_units} hours")
  elif num_of_days ==0:
    return("number 0 does not make sense")
  else:
    return("wrong input inserted")

def cleaning_up_code():
  if num_of_days.isdigit():
    user_input_number = int(num_of_days)
    calculated_value = days_to_units(user_input_number)
    print(calculated_value)
    print("\nthank you for participating")
  else:
    print("not a number")

user_input = ""
while user_input != "exit":
  user_input = input("Hey, put in a number of days and I will turn it into hours\n")
  for num_of_days in user_input.split(","):
    cleaning_up_code()
