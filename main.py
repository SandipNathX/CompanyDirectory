import addEmployee
import deleteEmployee
import readEmployee
import searchEmployee
import updateEmployee


def menuOptions():
    options = 0
    list = ["1", "2", "3", "4", "5", "6"]
    while options not in list:
        print(
            '\n\x1b[44m                                            '  + '\x1b[0m\n' 
            + '\x1b[44m' + '\x1b[30m' + '\x1b[1m' + '      Company Directory - Menu Options      '  + '\x1b[0m\n' 
            + '\x1b[44m                                            '   + '\x1b[0m\n' 
            + '\x1b[100m                                            ' +  '\x1b[0m\n' 
            + '\x1b[100m' + '\x1b[37m' + '  1. Show employees                         ' + '\x1b[0m\n' 
            + '\x1b[100m' + '\x1b[37m' + '  2. Add employee                           ' + '\x1b[0m\n' 
            + '\x1b[100m' + '\x1b[37m' + '  3. Update employee                        ' + '\x1b[0m\n' 
            + '\x1b[100m' + '\x1b[37m' + '  4. Search employee                        ' + '\x1b[0m\n' 
            + '\x1b[100m' + '\x1b[37m' + '  5. Delete employee                        ' + '\x1b[0m\n' 
            + '\x1b[100m' + '\x1b[37m' + '  6. Exit                                   ' + '\x1b[0m\n' 
            + '\x1b[100m                                            ' + '\x1b[0m\n'
        )

        options = input("\nPlease enter one of the options (1, 2, 3, 4, 5, 6) from the list above: ")

        if options not in list:
            print(f"\n\x1b[31mThe option {options} you have entered is not in the list above. Please try again.\x1b[0m")

    return options


mainProgram = True

while mainProgram == True:
    mainMenu = menuOptions()

    if mainMenu == "1":
        readEmployee.readEmployee()
        
    elif mainMenu == "2":
        addEmployee.addEmployee()

    elif mainMenu == "3":
        updateEmployee.updateEmployee()

    elif mainMenu == "4":
        searchEmployee.searchEmployee()

    elif mainMenu == "5":
        deleteEmployee.deleteEmployee()

    elif mainMenu == "6":
        # mainProgram == False
        break
# input("Press enter to exit ")
