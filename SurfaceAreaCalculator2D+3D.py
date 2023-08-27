# casonator was here
# Area calculator of 2D quadilateral:

from colorama import *
from time import sleep

Pi = 3.1415
Delay = 0.005

# function for 2D calcualtion
def TwoDimAreaCalc():
    Height = float(input("Enter height: " + Fore.GREEN));sleep(Delay)
    print(Fore.RESET + "Height set to " + Fore.BLUE  + str(Height) + Fore.RESET)
    Width = float(input("Enter width:" + Fore.GREEN));sleep(Delay)
    print(Fore.RESET + "Radius set to " + Fore.BLUE  + str(Width) + Fore.RESET)
    Area = Height * Width
    print (Fore.RESET + Style.BRIGHT + "\nThe area is " + Fore.YELLOW +  str(Area) + "\n")

# function for 3D calcualtion
def ThreeDimAreaCalc():
    Height2 = float(input("Enter height: " + Fore.GREEN));sleep(Delay)
    print(Fore.RESET + "Height set to " + Fore.BLUE + str(Height2) + Fore.RESET)
    Width2 = float(input("Enter width: " + Fore.GREEN));sleep(Delay)
    print(Fore.RESET + "Radius set to " + Fore.BLUE + str(Width2) + Fore.RESET)
    Depth = float(input("Enter depth: " + Fore.GREEN));sleep(Delay)
    print(Fore.RESET + "Depth set to " + str(Depth))
    DH = Depth * Height2
    SQAREA = Width2 * DH
    print (Fore.RESET + Style.BRIGHT + "\nSquare area of 3D right-angled quad: " + Fore.YELLOW + str(SQAREA) + "\n")

def Choose():

    Choice = int(input("Choose a selection.\n " + Fore.CYAN + "[ 1 ]" + Fore.RESET + " for square area calculation >

    if Choice == 2:
        ThreeDimAreaCalc()
        input(Fore.RESET + 'press enter to exit: ')

    elif Choice == 1:
        TwoDimAreaCalc()
        input(Fore.RESET + 'press enter to exit: ')

    else:
        print("Choose a valid option (1 or 2)")

Choose()
