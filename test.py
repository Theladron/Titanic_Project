def get_user_input(input_type):
    match input_type:
        case "type_int":
            while True:
                try:
                    user_input = (int(input("")))
                except ValueError:
                    print("Bitte geben Sie eine ganze Zahl ein.")
                else:
                    break
        case "type_float":
            while True:
                try:
                    user_input = (float(input("")))
                except ValueError:
                    print("Bitte geben Sie eine Zahl ein.")
                else:
                    break
    return user_input

print("Hier blabla Nutzeranweisungen blabla:")
zahl1 = get_user_input("type_int")