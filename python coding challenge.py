## PSEUDOCODE ##
## Create employee name variable (str)
## Create employee ID (str)
## Calculate gross pay ==> if salaried: salaried_pay = their_hourly_rate * 40 
    ## if hourly: hourly_pay = their_hourly_rate * hours_worked
## tax_rate = 22.0%
## Final amount after calculations ==> round() 
## Extract hire year from employee ID str using .slice
## Print total results

employee_name = "John Deo"
employee_ID = "XYZ-2026-CA"
is_salaried = True
hourly_rate = 54.99
hours_worked = 40.00
tax_rate = .22
gross_pay = round(hourly_rate * hours_worked, 2)
taxes_paid = round(gross_pay * tax_rate, 2)
net_pay = round(gross_pay - taxes_paid, 2) 

print(f"""Pay Stub
    Employee : {employee_name}
    ID : {employee_ID}
    Year Hired : {employee_ID[4:8]}
    Salaried : {is_salaried}
    Gross Pay : {gross_pay}
    Taxes : {taxes_paid}
    Net Pay : {net_pay}""")

