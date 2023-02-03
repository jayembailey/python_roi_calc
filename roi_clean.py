inc_list = []
class income(): 
    def __init__(self, units, rent):
        self.units = units
        self.rent = rent
    def calc(self):
        inc_list.append(self.units * self.rent)

def totalInc():
    return sum(inc_list)

exp_list = []
class expense(): 
    def __init__(self, cost):
        self.cost = cost
    def calc(self):
        exp_list.append(self.cost)

def totalExp():
    return sum(exp_list)

inv_list = []
class investment():
    def __init__(self, cost):
        self.cost = cost
    def calc(self):
        inv_list.append(self.cost)

def totalInv():
    return sum(inv_list)

def roi():
    return (acf / totalInv()) * 100

rentalInc = income(2, 1000)
rentalInc.calc()
laundryInc = income(2, 50)
laundryInc.calc()
storageInc = income(2, 200)
storageInc.calc()
print(f'Total income: ${totalInc()}/mo.')

taxes = expense(150)
taxes.calc()
insurance = expense(100)
insurance.calc()
utilities = expense(0)
utilities.calc()
vacancy_fund = expense(100)
vacancy_fund.calc()
repair_fund = expense(100)
repair_fund.calc()
capex_fund = expense(100)
capex_fund.calc()
mortgage = expense(860)
mortgage.calc()
prop_management = expense(200)
prop_management.calc()
print(f'Total expenses: ${totalExp()}/mo.')

acf = (totalInc() - totalExp()) * 12 #convert monthly to annual cash flow
print(f'Annual Cash Flow: ${acf}')

down_payment = investment(40000)
closing_cost = investment(3000)
rehab = investment(7000)
misc_other = investment(300)
down_payment.calc()
closing_cost.calc()
rehab.calc()
misc_other.calc()
print(f'Total initial investments: ${totalInv()}')

print(f'Cash on cash ROI: {roi()}%')