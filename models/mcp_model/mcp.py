import pandas as pd

class MCP:
    def __init__(self):
        pass

    def andMcp(self, data):
        xInput,wInput = self.validateData(data);
        theta = "and";
        return self.mcpModel(xInput,wInput,theta);

    def orMcp(self, data):
        xInput,wInput = self.validateData(data);
        theta = "or";
        return self.mcpModel(xInput,wInput,theta);

    def nandMcp(self, data):
        xInput,wInput = self.validateData(data);
        theta = "and";
        output = self.mcpModel(xInput,wInput,theta);
        return 0 if output == 1 else 1;

    def customThetaMcp(self, data, theta):
        xInput,wInput = self.validateData(data);
        return self.mcpModel(xInput,wInput,theta);

    def validateData(self, data):
        """check if the data is valid input for the mcp model"""
        csvFile = pd.read_csv(data,usecols=["x_input","weight_input"]);
        if csvFile.empty:
            raise ValueError("The data is empty")

        for x in csvFile["x_input"]:
            if x < 0 or x > 1:
                raise ValueError("Input contains unvalid values")
            if pd.isna(x):
                raise ValueError("Column contains NAN in X_Input. Check input file.");
        
        wInput = [];
        for w in csvFile["weight_input"]:
            if pd.isna(w):
                w = 1;
            wInput.append(w);
        
        xInput = csvFile["x_input"].tolist();

        print(xInput);
        print(wInput);

        return xInput,wInput;

    def mcpModel(self, xinput, winput, theta):
        """
        rows: list of Xn values
        theta: theta value
        """
        sum = 0;

        if theta == "and":
            theta = len(xinput);
            for x in xinput:
                sum += x;
        
        elif theta == "or":
            theta = 1;
            for x in xinput:
                sum += x;
        
        else:
            for i in range(len(xinput)):
                sum += xinput[i] * winput[i]; 

        if sum >= theta:
            return 1;
        else:
            return 0;

