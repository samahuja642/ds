# # problem A
# portion_down_payment = 0.25
# current_savings = 0
# r = 0.04
# annual_salary = float(input('Enter Your Annual Salary:'))
# monthly_salary = annual_salary/12
# portion_saved = float(input('Enter in percentage of money saved:'))
# total_cost = float(input('Enter Cost of Your Dream House : '))
# months = 0 
# while current_savings<portion_down_payment*total_cost:
#     current_savings = current_savings*(r/12)+ current_savings 
#     current_savings += portion_saved*monthly_salary
#     months+=1
# print(months)


# problem B
portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input('Enter Your Annual Salary:'))
monthly_salary = annual_salary/12
portion_saved = float(input('Enter in percentage of money saved:'))
total_cost = float(input('Enter Cost of Your Dream House : '))
months = 0 
semi_annual_raise = float(input("SEMI-ANNUAL RAISE : "))
while current_savings<portion_down_payment*total_cost:
    if months%6==0 and months!=0:
        annual_salary = (1+semi_annual_raise)*annual_salary
        monthly_salary = annual_salary/12
    current_savings = current_savings*(r/12)+ current_savings 
    current_savings += portion_saved*monthly_salary
    months+=1
print(months)