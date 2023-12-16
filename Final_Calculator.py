def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        print(user_input)

        if user_input.endswith('$'):
            return '$'
        elif user_input.endswith('#'):
            exit()
        else:
            return user_input


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")


    restart = False

    while True:
        choice = get_user_input("Enter choice (+, -, *, /, ^, %, #, $): ")
        if choice == '$':
            restart = True
            break
        if choice not in ("+", "-", "*", "/", "^", "%", '$'):
            print('Unrecognised operation')
            continue

        elif choice in ("+", "-", "*", "/", "^", "%", '$'):
            break

    if restart is True:
        continue


    while True:
        first_number = get_user_input('First number: ')
        if first_number == '$':
            restart =  True
            break
        try:
            first_operand = float(first_number)
            break

        except :
            print('unidentified operand')
            continue

    if restart is True:
        continue

    while True:
        second_number = get_user_input('Second number: ')
        if second_number == '$':
            restart = True
            break
        try:
            second_operand = float(second_number)
            break

        except:
            print('unidentified operand')
            continue
    if restart is True:
        continue

    if choice == '+':
        result = first_operand + second_operand
        print(result)

    elif choice == '-':
        result = first_operand - second_operand
        print(result)

    elif choice == '*':
        result = first_operand * second_operand
        print(result)

    elif choice == '/':
        try:
            result = first_operand/second_operand
            print(result)
        except:
            print("Can't divide by zero")

    elif choice == '^':
        result = first_operand ** second_operand
        print(result)

    elif choice == '%':
        result = first_operand % second_operand
        print(result)

    while True:
        proceed = input('Want to perform another calculation(Y/N)').upper()

        if proceed == 'Y':
            break
        elif proceed == 'N':
            exit()
        elif proceed.endswith('$'):
            boool = True
            break
        else:
            print('Unrecognised answer')
            continue
    if proceed == 'Y' or boool is True :
        continue


