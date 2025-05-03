from models.mcp_model.mcp import MCP;
print("Start machine learning models project!");


modelSelect = 0;

while(modelSelect != 99):
    print("\nWhich model want to test?");
    print("Input a number to select model.");
    print("1. mcp")
    print("2. percentron")
    print("3. ...")
    print("99. quit program")


    modelSelect = input("Your choice: ");
    val = 0;
    try:
        val = int(modelSelect);
    except ValueError:
        print("Selection must be number.")

    if val == 99:
        print("Quit Program");
        break;

    elif val == 1:
        print("You choose MCP model.")

    else:
        print("Other model is not READY yet. Sorry!")

    print("\nGive me the data path (must be csv file)");
    path = input("File Paht: ");

    match val:
        case 1:
            print("Start MCP Model!")
            mode = 0;
            while(mode != 99):
                print("\nWhich logic do you want to test?")
                print("1. AND")
                print("2. OR")
                print("3. NAND")
                print("4. CUSTOM THETA")
                print("99. Go Back")
                
                mode = input("your choice: ")
                mcp = MCP();

                try:
                    mode = int(mode);
                except ValueError:
                    print("Selection must be number.")

                match mode:
                    case 1:
                        print("run AND mcp model");
                        result = mcp.andMcp(path);
                    case 2:
                        print("run OR mcp model");
                        result = mcp.orMcp(path);
                    case 3:
                        print("run NAND mcp model");
                        result = mcp.nandMcp(path);
                    case 4:
                        print("run CUSTOM mcp model");
                        theta = input("What is your custom theta value?: ")
                        try:
                            theta = int(theta);
                        except ValueError:
                            print("Theta must be number.");
                        result = mcp.customThetaMcp(path,theta);
                    case 99:
                        print("go back to model select menu")
                        break;
                    case _:
                        print("Choose from option!")

                if result > 0:
                    print("MCP Model said YES!\n")
                else: print("MCP Model said NO!\n")

                print("Finish MCP Model Run");
                mode = 99;
                
                

            
        case _:
            print("");