def format_name(f_name, l_name):
    formated_first = f_name.title()
    formated_last = l_name.title()
    return f"{formated_first} {formated_last}"

User_First = input ("Tell me your first name: ").lower()
User_Last = input ("Tell me your last name: ").lower()
format_string = format_name(f_name=User_First, l_name=User_Last)
print(format_string)