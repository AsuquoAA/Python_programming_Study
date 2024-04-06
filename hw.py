lst_of_workers = []

for i in range(400):
    worker = {"Name":"Worker "+str(i+1),"Salary":7500+(i*55),"Gender":"Male" if i%2==0 else "Female"}
    lst_of_workers.append(worker) 

for worker in lst_of_workers:
    if worker["Salary"] > 7500 and worker["Salary"] < 30000:
        if worker["Gender"] == "Female":
            worker["Employee Level"] = "A5-F"
            print(worker)
        elif worker["Salary"] > 10000 and worker["Salary"] < 20000:
            if worker["Gender"] != "Female":
                worker["Employee Level"] = "A-1" 
                print(worker)
        else:
            worker["Employee Level"] = "blank"
            print(worker)       
    


import zipfile
with open("Total.csv","r") as homework:
    hw = homework.readlines()
  
def employeefunc(name):
    for lin in hw:
        if name in lin:
            return lin
salary_dict = {}  
header = hw[0]      
for lin in hw:
    if lin!=header:
        lins = lin.split(",")
        name = lins[0]
        salary = (lins[-7])
        salary_dict[name] = salary.strip()
try:
    employee_name = input("Enter employee name: ")
    employee_data = (employeefunc(employee_name))
    if employee_data is not None:
        with open("Employee Details.csv","w") as csvdata:
            csvdata.write(employeefunc(employee_name))    
        with zipfile.ZipFile("Employee_Profile.zip", "w") as zipf:
            zipf.write("Employee Details.csv")
        print("Employee details saved and zipped successfully.")
    else:
        print("Employee not found")        
except Exception:
    print("An error has occured")  

     
    
class policyholders:
    def __init__(self,name,policy_number,status = "NA"):
        self.name = name
        self.policy_number = policy_number
        self.status = status

    def register(self):
        self.status = "Active"
        print("Account registered successfully")    

    def suspended(self):
        self.status = "Suspended"
        print("Account  has been suspended")

    def reactivate(self):
        if self.status == "Suspended":
            self.status = "Active"
            print("Account has been reactivated")
        else:
            print("Cannot reactivate, account not suspended")    

    def display_details(self):
        print("Policy holder " + self.policy_number + " details")
        print("Name: " + self.name)
        print("Policy Number: " + self.policy_number)
        print("Status: " + self.status)    


class products:
    def __init__(self,name,price,status = "NA"):
        self.name = name
        self.price = price
        self.status = status

    def create(self):
        self.status = "Available"
        print("Product is available")    

    def remove(self):
        self.name = ""
        self.price = "NA"
        self.status = "NA"
        print("Product has been removed")

    def update(self,new_name,new_price):
        if self.status == "Available":
            self.name = new_name
            self.price = new_price
            print("Product has been updated")
        else:
            print("Cannot update suspended product")    


class Payment:
    def process_payment(self, amount):
        print("Payment processed successfully for amount:", amount)

    def send_reminder(self):
        print("Reminder sent for pending payment.")

    def apply_penalty(self):
        print("Penalty applied for late payment.")


customer1 = policyholders("John Doe", "POL-"+str(1))       
customer1.register()
customer1.display_details()