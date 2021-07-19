#IntegerChecker===================================================================================================================================
def int_check(string):
    try:
        int(string)
        return True
    except ValueError: 
        return False
#EmployeeID=======================================================================================================================================
def reg_EmployeeID():
    EmployeeID = ""
    while True:
        EmployeeID = input("Please enter an employee ID: ")
        EmployeeID = EmployeeID.strip()
        if len(EmployeeID) != 4 or not int_check(EmployeeID):
            print("\nEmployee ID must be four digits long.")
        if len(EmployeeID) == 4 and int_check(EmployeeID):
            cur.execute("SELECT EmployeeID FROM Employee WHERE EmployeeID = ?", (EmployeeID,))
            if len(cur.fetchall()) == 0:
                break
            else:
                print("\nEmployee ID is already registered.")
    return EmployeeID
        
#FirstName=======================================================================================================================================
def reg_FirstName():
    FirstName = ""
    while not FirstName:
        FirstName = input("Please enter employee's first name: ").replace(" ", "").replace("\t", "").lower().title()
        while not FirstName:
            print("\nFirst name field must not be blank.")
            FirstName = input("Please enter employee's first name: ")
            FirstName = FirstName.strip()
        return(FirstName)
        
#LastName========================================================================================================================================
def reg_LastName():
    LastName = ""
    while not LastName:
        LastName = input("Please enter employee's last name: ").replace(" ", "").replace("\t", "").lower().title()
        while not LastName:
            print("\nLast name field must not be blank.")
            LastName = input("Please enter employee's last name: ")
            LastName = LastName.strip()
        return(LastName)
        
#Email===========================================================================================================================================
def reg_Email():
    Email = ""
    while True:
        Email = input("Please enter employee's email: ")
        Email = Email.strip()
        if len(Email) == 0:    
            print("\nEmail field must not be blank.")
        else:
            cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + Email.lower() + "')")
            Email_Results = cur.fetchone()
            if Email_Results[0] != 0:
                return(Email)
            else:
                print("\nEmail is already being used.")
#Password========================================================================================================================================
def reg_Password():
    Password = ""
    while not Password:
        Password= input("Please enter new employee password: ")
        while not Password:
            print("\nPassword field must not be blank.")
            Password = input("Please enter new employee password: ")
            Password = Password.strip()
        return(Password)
        
#Register========================================================================================================================================
def register():
        print("\n")
        print(lines)
        print("\tWelcome New Employee!")
        print(lines)
        print("\n")
        query = "INSERT INTO Employee(EmployeeID, FirstName, LastName, Email, Password) VALUES(?,?,?,?,?)"
        cur.execute(query, (reg_EmployeeID(), reg_FirstName(), reg_LastName(), reg_Email(), reg_Password()))
        cur.fetchall()
        print("\n")
        print("Registration Successful!")
        print("1. Return to Main Menu \n2. Return to Login")
        register_input = ""
        while True:
            register_input =input ("\nPlease Select One of the Above :")
            if register_input == "1":
                return main_menu()
            elif register_input == "2":
                return login()
            else:
                print("\nError:")
                print("Please Input One of the Following Numbers")
        
#Login===========================================================================================================================================
def login():
    print("="*40)
    print("\nWelcome to Office Solutions")
    print("\nPlease Login Below ↓")
    print("="*40)    
    loginTest = False
    while not loginTest:
        try:
            userEmail = input("Please enter your email: ")
            userEmail = userEmail.strip()
            while not userEmail:
                userEmail = input("Please enter your email: ")
                userEmail = userEmail.strip()
                
            userPassword = input("Please enter your password: ")
            userPassword = userPassword.strip()
            while not userPassword:
                userPassword = input("Please enter your password: ")
                userPassword = userPassword.strip()
                
            cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + userEmail.lower() + "' AND Password = '" + userPassword.lower() + "')")
            results = cur.fetchone()
            if results[0] == 1:
                print("\nLogin successful")
                loginTest = True
                main_menu()
            else:
                print("\nLogin unsuccessful. Please try logging in again.")
        except:
            print("Connection failed")
#RegionPie=====================================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
xl = pd.ExcelFile("FA18SalesData.xlsx")
SalesData = xl.parse("Orders")
Total_Region_Sales = SalesData[["Region", "Sales"]]
TotalSales = Total_Region_Sales.groupby(["Region"]).sum().sort_values(["Sales"], ascending = False).reset_index() 
lines = "="*50
#FurnitureTotal================================================================
Total_Furn_Sales = SalesData[["Category", "Sales"]]
Total_Furn = Total_Furn_Sales.loc[Total_Furn_Sales["Category"]=="Furniture"]
Furniture = Total_Furn.groupby(by="Category").sum().sort_values(by="Sales", ascending = False)
#OfficeSuppliesTotal===========================================================
Total_OS_Sales = SalesData[["Category", "Sales"]]
Total_OS = Total_Furn_Sales.loc[Total_OS_Sales["Category"]=="Office Supplies"]
OfficeSupplies = Total_OS.groupby(by="Category").sum().sort_values(by="Sales", ascending = False)
#TechnologyTotal===============================================================
Total_Tech_Sales = SalesData[["Category", "Sales"]]
Total_Tech = Total_Tech_Sales.loc[Total_Tech_Sales["Category"]=="Technology"]
Technology = Total_Tech.groupby(by="Category").sum().sort_values(by="Sales", ascending = False)
#MainRegionMenu================================================================
def RegionSales():
    print("\n")
    print(lines)
    print("\n")
    print("""\t1. West Region
          \n\t2. East Region
          \n\t3. South Region
          \n\t4. Central Region
          \n\t5. Return to Main Menu""")
    Region_Input = input("Please enter the region you would like to see: ")
    if Region_Input == "1":
        WestRegion()
    elif Region_Input== "2":
        EastRegion()
    elif Region_Input == "3":
        SouthRegion()
    elif Region_Input == "4":
        CentralRegion()
    elif Region_Input == "5":
        main_menu()
    else:
        print("\nError:")
        print("Please Enter a Number from 1 to 5")
        return RegionSales()
#WestRegion====================================================================
def WestRegion():
    print("\n")
    print(lines)
    print("West Region")
    print(lines)
    print("""\t1. Total West Region Sales
          \n\t2. Furniture Sales
          \n\t3. Office Supply Sales
          \n\t4. Technology Sales
          \n\t5. Return to Region Sales Main Menu
          \n\t6. Return to Main Menu""")
    West_Input = input("Please enter the sales category you would like to see: ")
    if West_Input == "1":
        West_Sales = SalesData[["Region", "Sales"]]
        West_Sales_Sum = West_Sales.loc[West_Sales["Region"]=="West"]
        TotalWest_Sales = West_Sales_Sum.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print("\n")
        print(lines)
        print("\nThe total West region sales is:")
        print(TotalWest_Sales)
        labels = list(TotalSales.Region.values)
        values = list(TotalSales.Sales.values)
        explode = (0.1,0,0,0)
        plt.figure(figsize=(7,7))
        plt.title("West Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        print("\n")
        print(lines)
        ReturnMenu()
    elif West_Input == "2":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_Furn = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="West"]
        Furn_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Furniture"]
        RegionFurniture = Region_Furn.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionFurn = Furn_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Furniture sales in all regions is: ")
        print(RegionFurn)
        print(lines)
        print(Furniture)
        labels = list(RegionFurniture.Category.values)
        values = list(RegionFurniture.Sales.values)
        explode = (0.1,0,0)
        plt.figure(figsize=(7,7))
        plt.title("West Furniture Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif West_Input == "3":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_OS = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="West"]
        OS_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Office Supplies"]
        RegionOfficeSupplies = Region_OS.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionOS = OS_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Office Supplies sales in all regions is: ")
        print(RegionOS)
        print(lines)
        print(OfficeSupplies)
        labels = list(RegionOfficeSupplies.Category.values)
        values = list(RegionOfficeSupplies.Sales.values)
        explode = (0,0.1,0)
        plt.figure(figsize=(7,7))
        plt.title("West Office Supplies Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif West_Input == "4":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_Tech = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="West"]
        Tech_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Technology"]
        RegionTechnology = Region_Tech.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionTech = Tech_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Office Supplies sales in all regions is: ")
        print(RegionTech)
        print(lines)
        print(Technology)
        labels = list(RegionTechnology.Category.values)
        values = list(RegionTechnology.Sales.values)
        explode = (0,0,0.1)
        plt.figure(figsize=(7,7))
        plt.title("West Technology Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif West_Input == "5":
        RegionSales()
    elif West_Input == "6":
        main_menu()
    else:
        print("\nError:")
        print("Please Enter a Number from 1 to 6")
        return WestRegion()
#EastRegion====================================================================
def EastRegion():
    print("\n")
    print(lines)
    print("East Region")
    print(lines)
    print("""\t1. Total East Region Sales
          \n\t2. Furniture Sales
          \n\t3. Office Supply Sales
          \n\t4. Technology Sales
          \n\t5. Return to Region Sales Main Menu
          \n\t6. Return to Main Menu""")
    East_Input = input("Please enter the sales category you would like to see: ")
    if East_Input == "1":
        East_Sales = SalesData[["Region", "Sales"]]
        East_Sales_Sum = East_Sales.loc[East_Sales["Region"]=="East"]
        TotalEast_Sales = East_Sales_Sum.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print("\n")
        print(lines)
        print("\nThe total East region sales is:")
        print(TotalEast_Sales)
        labels = list(TotalSales.Region.values)
        values = list(TotalSales.Sales.values)
        explode = (0,0.1,0,0)
        plt.figure(figsize=(7,7))
        plt.title("East Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif East_Input == "2":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_Furn = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="East"]
        Furn_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Furniture"]
        RegionFurniture = Region_Furn.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionFurn = Furn_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Furniture sales in all regions is: ")
        print(RegionFurn)
        print(lines)
        print(Furniture)
        labels = list(RegionFurniture.Category.values)
        values = list(RegionFurniture.Sales.values)
        explode = (0.1,0,0)
        plt.figure(figsize=(7,7))
        plt.title("East Furniture Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif East_Input == "3":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_OS = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="East"]
        OS_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Office Supplies"]
        RegionOfficeSupplies = Region_OS.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionOS = OS_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Office Supplies sales in all regions is: ")
        print(RegionOS)
        print(lines)
        print(OfficeSupplies)
        labels = list(RegionOfficeSupplies.Category.values)
        values = list(RegionOfficeSupplies.Sales.values)
        explode = (0,0.1,0)
        plt.figure(figsize=(7,7))
        plt.title("East Office Supplies Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif East_Input == "4":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_Tech = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="East"]
        Tech_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Technology"]
        RegionTechnology = Region_Tech.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionTech = Tech_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Office Supplies sales in all regions is: ")
        print(RegionTech)
        print(lines)
        print(Technology)
        labels = list(RegionTechnology.Category.values)
        values = list(RegionTechnology.Sales.values)
        explode = (0,0,0.1)
        plt.figure(figsize=(7,7))
        plt.title("East Technology Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif East_Input == "5":
        RegionSales()
    elif East_Input == "6":
        main_menu()
    else:
        print("\nError:")
        print("Please Enter a Number from 1 to 6")
        return EastRegion()
#SouthRegion===================================================================
def SouthRegion():
    print("\n")
    print(lines)
    print("South Region")
    print(lines)
    print("""\t1. Total South Region Sales
          \n\t2. Furniture Sales
          \n\t3. Office Supply Sales
          \n\t4. Technology Sales
          \n\t5. Return to Region Sales Main Menu
          \n\t6. Return to Main Menu""")
    South_Input = input("Please enter the sales category you would like to see: ")
    if South_Input == "1":
        South_Sales = SalesData[["Region", "Sales"]]
        South_Sales_Sum = South_Sales.loc[South_Sales["Region"]=="South"]
        TotalSouth_Sales = South_Sales_Sum.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print("\n")
        print(lines)
        print("\nThe total South region sales is:")
        print(TotalSouth_Sales)
        labels = list(TotalSales.Region.values)
        values = list(TotalSales.Sales.values)
        explode = (0,0,0,0.1)
        plt.figure(figsize=(7,7))
        plt.title("South Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif South_Input == "2":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_Furn = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="South"]
        Furn_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Furniture"]
        RegionFurniture = Region_Furn.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionFurn = Furn_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Furniture sales in all regions is: ")
        print(RegionFurn)
        print(lines)
        print(Furniture)
        labels = list(RegionFurniture.Category.values)
        values = list(RegionFurniture.Sales.values)
        explode = (0.1,0,0)
        plt.figure(figsize=(7,7))
        plt.title("South Furniture Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif South_Input == "3":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_OS = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="South"]
        OS_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Office Supplies"]
        RegionOfficeSupplies = Region_OS.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionOS = OS_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Office Supplies sales in all regions is: ")
        print(RegionOS)
        print(lines)
        print(OfficeSupplies)
        labels = list(RegionOfficeSupplies.Category.values)
        values = list(RegionOfficeSupplies.Sales.values)
        explode = (0,0.1,0)
        plt.figure(figsize=(7,7))
        plt.title("South Office Supplies Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif South_Input == "4":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_Tech = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="South"]
        Tech_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Technology"]
        RegionTechnology = Region_Tech.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionTech = Tech_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Office Supplies sales in all regions is: ")
        print(RegionTech)
        print(lines)
        print(Technology)
        labels = list(RegionTechnology.Category.values)
        values = list(RegionTechnology.Sales.values)
        explode = (0,0,0.1)
        plt.figure(figsize=(7,7))
        plt.title("South Technology Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif South_Input == "5":
        RegionSales()
    elif South_Input == "6":
        main_menu()
    else:
        print("\nError:")
        print("Please Enter a Number from 1 to 6")
        return SouthRegion()
#CentralRegion=================================================================
def CentralRegion():
    print("\n")
    print(lines)
    print("Central Region")
    print(lines)
    print("""\t1. Total Central Region Sales
          \n\t2. Furniture Sales
          \n\t3. Office Supply Sales
          \n\t4. Technology Sales
          \n\t5. Return to Region Sales Main Menu
          \n\t6. Return to Main Menu""")
    Central_Input = input("Please enter the sales category you would like to see: ")
    if Central_Input == "1":
        Central_Sales = SalesData[["Region", "Sales"]]
        Central_Sales_Sum = Central_Sales.loc[Central_Sales["Region"]=="Central"]
        TotalCentral_Sales = Central_Sales_Sum.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print("\n")
        print(lines)
        print("\nThe total Central region sales is:")
        print(TotalCentral_Sales)
        labels = list(TotalSales.Region.values)
        values = list(TotalSales.Sales.values)
        explode = (0,0,0.1,0)
        plt.figure(figsize=(7,7))
        plt.title("Central Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif Central_Input == "2":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_Furn = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="Central"]
        Furn_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Furniture"]
        RegionFurniture = Region_Furn.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionFurn = Furn_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Furniture sales in all regions is: ")
        print(RegionFurn)
        print(lines)
        print(Furniture)
        labels = list(RegionFurniture.Category.values)
        values = list(RegionFurniture.Sales.values)
        explode = (0.1,0,0)
        plt.figure(figsize=(7,7))
        plt.title("Central Furniture Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif Central_Input == "3":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_OS = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="Central"]
        OS_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Office Supplies"]
        RegionOfficeSupplies = Region_OS.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionOS = OS_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Office Supplies sales in all regions is: ")
        print(RegionOS)
        print(lines)
        print(OfficeSupplies)
        labels = list(RegionOfficeSupplies.Category.values)
        values = list(RegionOfficeSupplies.Sales.values)
        explode = (0,0.1,0)
        plt.figure(figsize=(7,7))
        plt.title("Central Office Supplies Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif Central_Input == "4":
        Region_Cate_Sales = SalesData[["Region", "Category", "Sales"]]
        Region_Tech = Region_Cate_Sales.loc[Region_Cate_Sales["Region"]=="Central"]
        Tech_Cate = Region_Cate_Sales.loc[Region_Cate_Sales["Category"]=="Technology"]
        RegionTechnology = Region_Tech.groupby(by="Category").sum(by="Sales").sort_values(by="Category").reset_index()
        RegionTech = Tech_Cate.groupby(by="Region").sum().sort_values(by="Sales", ascending = False)
        print(lines)
        print("\n")
        print("\nThe total Office Supplies sales in all regions is: ")
        print(RegionTech)
        print(lines)
        print(Technology)
        labels = list(RegionTechnology.Category.values)
        values = list(RegionTechnology.Sales.values)
        explode = (0,0,0.1)
        plt.figure(figsize=(7,7))
        plt.title("Central Technology Sales Percentages")
        plt.pie(values, labels=labels, explode=explode, shadow=True, autopct = '%1.1f%%')
        plt.show()
        ReturnMenu()
    elif Central_Input == "5":
        RegionSales()
    elif Central_Input == "6":
        main_menu()
    else:
        print("\nError:")
        print("Please Enter a Number from 1 to 6")
        return CentralRegion()
#ReturnMenuSale====================================================================
def ReturnMenu():
    Return_Input = input("""\t1. Test Another Region
                         \n\t2. Return to Main Menu
                         \nPlease enter one of the above: """)
    if Return_Input == "1":
        return RegionSales()
    elif Return_Input == "2":
        main_menu()
    else:
        print("Error:")
        print("Please enter 1 or 2")
        return ReturnMenu()  
#WestDiscountuity==============================================================
def West_Dis():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    wquant= SalesData[["Profit", "Region", "Sub-Category"]]
    sub_wquant= wquant.loc[wquant["Region"]== "West"]
    reg_wquant=sub_wquant.groupby(by="Sub-Category").sum().sort_values(by="Profit", ascending=False)
    reg_wquant=reg_wquant.reset_index()
    barchart4 = sns.barplot(x="Sub-Category", y="Profit", data=reg_wquant)
    barchart4.set_xticklabels(barchart4.get_xticklabels(), rotation=75)
    barchart4.set_title("Profit by Sub-Category")
    print("\n")
    print(lines)
    print("\nLowest sub-category in terms of profit in the West region is: ")
    print (reg_wquant.tail(5))
    plt.show()
    ReturnMenuDis()
#EastDiscountuity==============================================================
def East_Dis():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    equant= SalesData[["Profit", "Region", "Sub-Category"]]
    sub_equant= equant.loc[equant["Region"]== "East"]
    reg_equant=sub_equant.groupby(by="Sub-Category").sum().sort_values(by="Profit", ascending=False)
    reg_equant=reg_equant.reset_index()
    barchart3 = sns.barplot(x="Sub-Category", y="Profit", data=reg_equant)
    barchart3.set_xticklabels(barchart3.get_xticklabels(), rotation=75)
    barchart3.set_title("Profit by Sub-Category")
    print("\n")
    print(lines)
    print("\nLowest sub-category in terms of profit in the East region is: ")
    print (reg_equant.tail(5))
    plt.show()
    ReturnMenuDis()
#SouthDiscountuity=============================================================
def South_Dis():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    squant= SalesData[["Profit", "Region", "Sub-Category"]]
    sub_squant= squant.loc[squant["Region"]== "South"]
    reg_squant=sub_squant.groupby(by="Sub-Category").sum().sort_values(by="Profit", ascending=False)
    reg_squant=reg_squant.reset_index()
    barchart2=sns.barplot(x="Sub-Category", y="Profit", data=reg_squant)
    barchart2.set_xticklabels(barchart2.get_xticklabels(), rotation=75)
    barchart2.set_title("Profit by Sub-Category")
    print("\n")
    print(lines)
    print("\nLowest sub-category in terms of profit in the South region is: ")
    print (reg_squant.tail(5))
    plt.show()
    ReturnMenuDis()
#CentralDiscountuity===========================================================
def Central_Dis():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    cquant= SalesData[["Profit", "Region", "Sub-Category"]]
    sub_cquant= cquant.loc[cquant["Region"]== "Central"]
    reg_cquant=sub_cquant.groupby(by="Sub-Category").sum().sort_values(by="Profit", ascending=False)
    reg_cquant=reg_cquant.reset_index()
    barchart1=sns.barplot(x= "Sub-Category", y= "Profit", data=reg_cquant)
    barchart1.set_xticklabels(barchart1.get_xticklabels(), rotation=75)
    barchart1.set_title("Profit by Sub-Category")
    print("\n")
    print(lines)
    print("\nLowest sub-category in terms of profit in the Central region is: ")
    print (reg_cquant.tail(5))
    plt.show()
    ReturnMenuDis()
#DiscountProfit================================================================
def Dis_Pro():
    import pandas as  pd
    import scipy.stats
    import matplotlib.pyplot as plt
    import warnings
    warnings.filterwarnings('ignore')
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    CopySalesData=SalesData.copy()
    x="Discount"
    y="Profit"
    scipy.stats.spearmanr(CopySalesData[x], CopySalesData[y])
    print("\n")
    print(lines)
    print("This graph shows the correlation between Discounts and Profits: ")
    plt.scatter(x=x, y=y, data=CopySalesData)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("Correlations of " +x+ " and " + y)
    plt.pause(0.1)
    plt.show()
    ReturnFullMenu()
#DiscountQuantity================================================================
def Dis_Quant():
    import pandas as  pd
    import scipy.stats
    import matplotlib.pyplot as plt
    import warnings
    warnings.filterwarnings('ignore')
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    CopySalesData=SalesData.copy()
    x="Discount"
    y="Quantity"
    scipy.stats.pearsonr(CopySalesData[x], CopySalesData[y])
    print("\n")
    print(lines)
    print("This graph shows the correlation between Discounts and Quantities: ")
    plt.scatter(x=x, y=y, data=CopySalesData)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("Correlations of " +x+ " and " + y)
    plt.pause(0.1)
    plt.show()
    ReturnFullMenu()
#ReturnMenuDis=================================================================
def ReturnMenuDis():
    Return_Input = input("""\t1. Test Another Region
                         \n\t2. Return to Main Menu
                         \nPlease enter one of the above: """)
    if Return_Input == "1":
        return RegionDis()
    elif Return_Input == "2":
        main_menu()
    else:
        print("Error:")
        print("Please enter 1 or 2")
        return ReturnMenuDis()    
#MainDisMenu================================================================
def RegionDis():
    print("\n")
    print(lines)
    print("\n")
    print("""\t1. West Region
          \n\t2. East Region
          \n\t3. South Region
          \n\t4. Central Region
          \n\t5. Return to Main Menu""")
    Region_Input = input("Please enter the region you would like to see: ")
    if Region_Input == "1":
        West_Dis()
    elif Region_Input== "2":
        East_Dis()
    elif Region_Input == "3":
        South_Dis()
    elif Region_Input == "4":
        Central_Dis()
    elif Region_Input == "5":
        return main_menu()
    else:
        print("\nError:")
        print("Please Enter a Number from 1 to 5")
        return RegionDis()    
#Loyalty'sProgramPandas========================================================
import pandas as pd
xl = pd.ExcelFile("FA18SalesData.xlsx")
SalesData = xl.parse("Orders")
Customer = SalesData["Customer Name"].value_counts()
Total_Customers = Customer.shape
Top_10Percent = int(Total_Customers[0]*.1)
Top_5Percent = int(Total_Customers[0]*.05)
Top_1Percent = int(Total_Customers[0]*.01)
#CustomerInputMenu=============================================================
def Cust_Input_Menu():
    print("""\n\t1. Customers who buy more frequent
          \n\t2. Customers who buy the most quantity
          \n\t3. Return to Main Menu""")
    Customer_Input = input("Please select one of the above: ")
    if Customer_Input == "1":
        Customer_Frequency()
    elif Customer_Input == "2":
        Customer_Quantity()
    elif Customer_Input == "3":
        main_menu()
    else:
        print("Error:")
        print("Please enter a number from 1 to 3")
        return Cust_Input_Menu()
#Frequency=====================================================================
def Customer_Frequency():
    print("""\n\t1. Top 10 Percent of Customers
          \n\t2. Top 5 Percent of Customers
          \n\t3. Top 1 Percent of Customers
          \n\t4. Return to Loyalty's Program Menu
          \n\t5. Return to Main Menu""")
    Customer_Freq_Input = input("Please select one of the above to view Customers: ")
    if Customer_Freq_Input == "1":
        print("\n")
        print("These are the top 10 percent of customers who buy more frequent: ")
        print(lines)
        print(Customer.head(Top_10Percent))
        ReturnCust()
    elif Customer_Freq_Input == "2":
        print("\n")
        print("These are the top 5 percent of customers who buy more frequent: ")
        print(lines)
        print(Customer.head(Top_5Percent))
        ReturnCust()
    elif Customer_Freq_Input == "3":
        print("\n")
        print("These are the top 1 percent of customers who buy more frequent: ")
        print(lines)
        print(Customer.head(Top_1Percent))
        ReturnCust()
    elif Customer_Freq_Input == "4": 
        return Cust_Input_Menu
    elif Customer_Freq_Input == "5":
        main_menu()
    else:
        print("Error:")
        print("Please enter a number from 1 to 5")
        return Customer_Frequency()
#Quantity======================================================================
def Customer_Quantity():
    Customer_Quant = SalesData[["Customer Name", "Quantity"]]
    QuantitySize = Customer_Quant.groupby(by = "Customer Name").sum().sort_values(by = "Quantity", ascending = False)
    print("""\n\t1. Top 10 Percent of Customers
          \n\t2. Top 5 Percent of Customers
          \n\t3. Top 1 Percent of Customers
          \n\t4. Return to Loyalty's Program Menu
          \n\t5. Return to Main Menu""")
    Customer_Quant_Input = input("Please select one of the above to view Customers: ")
    if Customer_Quant_Input == "1":
        print("\n")
        print("These are the top 10 percent of customers who buy most quantity: ")
        print(lines)
        print(QuantitySize.head(Top_10Percent))
        ReturnCust()
    elif Customer_Quant_Input == "2":
        print("\n")
        print("These are the top 5 percent of customers who buy most quantity: ")
        print(lines)
        print(QuantitySize.head(Top_5Percent))
        ReturnCust()
    elif Customer_Quant_Input == "3":
        print("\n")
        print("These are the top 1 percent of customers who buy most quantity: ")
        print(lines)
        print(QuantitySize.head(Top_1Percent))
        ReturnCust()
    elif Customer_Quant_Input == "4": 
        return Cust_Input_Menu
    elif Customer_Quant_Input == "5":
        main_menu()
    else:
        print("Error:")
        print("Please enter a number from 1 to 5")
        return Customer_Quantity()
#ReturnCust====================================================================
def ReturnCust():
    Return_Input = input("""\n\t1. View other percentage of Customers
                         \n\t2. Return to Main Menu
                         \nPlease enter one of the above: """)
    if Return_Input == "1":
        return Cust_Input_Menu()
    elif Return_Input == "2":
        main_menu()
    else:
        print("Error:")
        print("Please enter 1 or 2")
        return ReturnCust() 
#ReturnMenu=================================================================
def ReturnFullMenu():
    Return_Input = input("""\t1. Return to Main Menu
                         \nPlease enter 1. to return to Main Menu: """)
    if Return_Input == "1":
        return main_menu()
    else:
        print("Error:")
        print("Please enter 1")
        return ReturnFullMenu()
#Main Menu=======================================================================================================================================
def main_menu():
    print("\n")
    print("="*43)
    print("\tWelcome to Office Solutions")
    print("="*43)
    print("\n")
    menu_inputs()
        
#Menu Inputs=====================================================================================================================================
def menu_inputs():
    print("""\t1. Register New Employee 
                     \n\t2. View the Least Profitable Products
                     \n\t3. View Correlation between Discounts and Profit
                     \n\t4. View Correlation between Discounts and Quantity
                     \n\t5. View Regional Sales and Product Category Sales
                     \n\t6. View Customers Eligible for Loyalty's Program
                     \n\t7. Exit to Login
                     \n\t8. Quit Application""")
    menu = input("\nPlease Enter One of the Above: ")
    if menu == "1":
        register()
    elif menu == "2":
        RegionDis()
    elif menu == "3":
        Dis_Pro()
    elif menu == "4":
        Dis_Quant()
    elif menu == "5":
        RegionSales()
    elif menu == "6":
        Cust_Input_Menu()
    elif menu == "7":
        login()
    elif menu == "8":
        exit()
    else:
        print("\nError:")
        print("Please Enter a Number from 1 to 8")
        print("\n")
        return menu_inputs()
#Main Program====================================================================================================================================
import sqlite3
conn = sqlite3.connect("OS_Employee.db")
with conn:
    cur = conn.cursor()
    try:
        login()
    except sqlite3.Error as er:
        print(er)
        print("Connection failed")
conn.close()