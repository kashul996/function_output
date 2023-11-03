def format_name(f_name,l_name):
  format_f_name=f_name.title()
  format_l_name=l_name.title()
  return f"{format_f_name} {format_l_name}"
format_string=format_name("rahuL","SingH")
print(format_string)
print(format_name("rahuL","SingH"))


def format_name(f_name,l_name):
  if f_name == "" or l_name=="":
    return "You didn't provide valid input"
  format_f_name=f_name.title()
  format_l_name=l_name.title()
  return f"{format_f_name} {format_l_name}"
#format_string=format_name("rahuL","SingH")
print(format_name(input("Type your first name: \n"),input("Type your last name:\n")))
#(format_string)