import os , subprocess
name = os.getenv("INSTANCE")

class virtual_diskspace:
    C = f"{os.getcwd()}\\VirtualMachines\\{name}"
    B = f"{os.getcwd()}\\EXTERNAL_DRIVES\\B"
    D = f"{os.getcwd()}\\EXTERNAL_DRIVES\\D"
    E = f"{os.getcwd()}\\EXTERNAL_DRIVES\\E"
    X = f"{os.getcwd()}\\EXTERNAL_DRIVES\\X"

def vmpath() -> str:
    return os.getcwd().replace(virtual_diskspace.C , "C:").replace(virtual_diskspace.B , "B:").replace(virtual_diskspace.D , "D:").replace(virtual_diskspace.E , "E:").replace(virtual_diskspace.X , "X:")
def range() -> bool:
    if (os.getcwd().startswith(virtual_diskspace.C)) or (os.getcwd().startswith(virtual_diskspace.B)) or (os.getcwd().startswith(virtual_diskspace.D)) or (os.getcwd().startswith(virtual_diskspace.E)) or (os.getcwd().startswith(virtual_diskspace.X)):
        return True
    else:
        return False

os.chdir(virtual_diskspace.C)
os.system(f"title DosVM - {name}")
while True:
    try:
        if range() == False:
            os.chdir(virtual_diskspace.C)
        if vmpath() == "C:":
            userinput = str(input(f"{vmpath()}\\>")).lower().replace("c:",virtual_diskspace.C).replace("b:",virtual_diskspace.B).replace("d:",virtual_diskspace.D).replace("e:",virtual_diskspace.E).replace("x:",virtual_diskspace.X)
        else:
            userinput = str(input(f"{vmpath()}>")).lower().replace("c:", virtual_diskspace.C).replace("b:",
                                                                                                        virtual_diskspace.B).replace(
                "d:", virtual_diskspace.D).replace("e:", virtual_diskspace.E).replace("x:", virtual_diskspace.X)
        if ("taskkill" in userinput) or ("diskpart" in userinput) or ("assign" in userinput) or ("cmd" in userinput):
            print("Denial: THIS IS FORBIDDEN IN DosVM")
        else:
            if userinput.startswith("cd "):
                os.chdir(userinput.lstrip("cd "))
            elif userinput == "cls":
                os.system("cls")
            elif userinput.startswith("del "):
                try:
                    os.remove(userinput.lstrip("del "))
                except:
                    os.removedirs(userinput.lstrip("del "))
            elif (userinput == "start calc.exe") or (userinput == "start calc") or (userinput == "calc.exe") or (userinput == "calc"):
                a = float(input("First number: "))
                b = float(input("Second number: "))
                print("1.Adding\n2.Substract\n3.Divide\n4.Multiply\n5.First number to the power of second number\n6. Square root of first number degree second number")
                operation = int(input("Select a number: "))
                if operation == 1:
                    print(f"{a}+{b} = {a+b}")
                elif operation == 2:
                    print(f"{a}-{b} = {a - b}")
                elif operation == 3:
                    print(f"{a}/{b} = {a / b}")
                elif operation == 4:
                    print(f"{a}*{b} = {a * b}")
                elif operation == 5:
                    print(f"{round(a)} to the power of {round(b)} = {round(a)^round(b)}")
                elif operation == 6:
                    print(f" {round(b)}√{round(a)} = {round(a)**(1/round(b))}")
            elif (userinput == "exit") or (userinput == "shutdown"):
                exit()
            else:
                result = subprocess.run(userinput,shell=True, capture_output=True, text=True)
                print(result.stdout.replace(virtual_diskspace.C , "C:\\").replace(virtual_diskspace.B , "B:\\").replace(virtual_diskspace.D , "D:\\").replace(virtual_diskspace.E , "E:\\").replace(virtual_diskspace.X , "X:\\"))
    except:
        os.system("cls")
        os.system("color 17")
        print("""A error has occurred.
Press enter to continue""")
        input()
        os.system("color 07")
        os.system("cls")

