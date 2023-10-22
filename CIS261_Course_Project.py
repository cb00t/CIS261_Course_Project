#Christopher Loe
#CSI261
#Course Project

def getEmpName():
    EmpName = input("Enter employee name: ")
    return EmpName

def getHoursWorked():
    HoursWorked = float(input("Enter Hours: "))
    return HoursWorked

def getHourlyRate():
    HourlyRate = float(input("Enter Hourly Rate: "))
    return HourlyRate

def getTaxRate():
     TaxRate = float(input("Enter Tax Rate: "))
     TaxRate = TaxRate / 100
     return TaxRate

def CalcTaxAndNetPay(HoursWorked, HourlyRate, TaxRate):
    GrossPay = HoursWorked * HourlyRate
    IncomeTax = GrossPay * TaxRate
    NetPay = GrossPay - IncomeTax
    return GrossPay, IncomeTax, NetPay

def printinfo(EmpName, HoursWorked, HourlyRate, GrossPay, TaxRate, IncomeTax, NetPay):
    print(EmpName, f"{HoursWorked:,.2f}", f"{HourlyRate:,.2f}", f"{GrossPay:,.2f}", f"{TaxRate:,.1%}", f"{IncomeTax:,.2f}", f"{NetPay:,.2f}")

def PrintTotals(TotalEmployees, TotalHours, TotalGrossPay, TotalTax, TotalNetPay):
    print(f"\nTotal Number Of Employees: {TotalEmployees}")
    print(f"Total Hours: {TotalHours:,.2f}")
    print(f"Total Gross Pay: {TotalGrossPay:,.2f}")
    print(f"Total Tax: {TotalTax:,.2f}")
    print(f"Total Net Pay: {TotalNetPay:,.2f}")

if __name__ == "__main__":
    TotalEmployees = 0
    TotalHours = 0.00
    TotalGrossPay = 0.00
    TotalTax = 0.00
    TotalNetPay = 0.00
    while True:
        EmpName = getEmpName()
        if EmpName.upper() == "END":
            break

        HoursWorked = getHoursWorked()
        HourlyRate = getHourlyRate()
        TaxRate = getTaxRate()
        GrossPay, IncomeTax, NetPay = CalcTaxAndNetPay(HoursWorked, HourlyRate, TaxRate)
        printinfo(EmpName, HoursWorked, HourlyRate, GrossPay, TaxRate, IncomeTax, NetPay)
        TotalEmployees += 1
        TotalHours += HoursWorked
        TotalGrossPay += GrossPay
        TotalTax += IncomeTax
        TotalNetPay += NetPay
    PrintTotals(TotalEmployees, TotalHours, TotalGrossPay, TotalTax, TotalNetPay)
