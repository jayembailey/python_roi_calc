class RoiCalc():
    def __init__(self):
        self = self

    def inc_query(self):
        inc_list = []
        rental_units = float(input('How many units are in the rental?'))
        rental_rent = float(input('What is the monthly rent per unit?'))
        inc_list.append(rental_units * rental_rent)
        while True:
            misc_inc = input('Does the property generate any other monthly incomes? y/n: ')
            if misc_inc.lower() == 'y':
                misc_unit = float(input('From how many sources is this income derived? '))
                misc_rent = float(input('What is the monthly income of each source?'))
                inc_list.append(misc_unit * misc_rent)
            elif misc_inc.lower() == 'n':
                break
            else:
                print('Please enter "y" or "n": ')
        return sum(inc_list)

    def exp_query(self):
        exp_list = []
        taxes = float(input('Please enter your annual tax payments: ')) / 12
        exp_list.append(taxes)
        insurance = float(input('Please enter monthly insurance payment: '))
        exp_list.append(insurance)
        utilities = float(input('Please enter monthly utility payments: '))
        exp_list.append(utilities)
        vacancy = float(input('Please enter monthly vacancy fund contribution: '))
        exp_list.append(vacancy)
        repairs = float(input('Please enter monthly repair fund contribution: '))
        exp_list.append(repairs)
        capex = float(input('Please enter monthly CapEx fund contribution: '))
        exp_list.append(capex)
        mortgage = float(input('Please enter monthly mortgage payment: '))
        exp_list.append(mortgage)
        mgmt = float(input('Please enter monthly management expenses: '))
        exp_list.append(mgmt)
        misc_exp = float(input('Please enter amount of any other monthly expenses: '))
        exp_list.append(misc_exp)
        return sum(exp_list)

    def inv_query(self):
        inv_list = []
        down_payment = float(input('Please enter your down payment: '))
        inv_list.append(down_payment)
        closing_cost = float(input('Please enter your closing costs: '))
        inv_list.append(closing_cost)
        rehab = float(input('Please enter your total rehab expenses: '))
        inv_list.append(rehab)
        misc_initial = float(input('Please enter any other initial investement costs: '))
        inv_list.append(misc_initial)
        return sum(inv_list)
    
    def run(self):
        total_inc = RoiCalc().inc_query()
        total_exp = RoiCalc().exp_query()
        total_inv = RoiCalc().inv_query()
        final = ((total_inc - total_exp)*12) / total_inv
        print(f'\nAnnual income: {total_inc * 12}')
        print(f'Annual expenses: {total_exp * 12}')
        print(f'Initial investment: {total_inv}')
        print(f'\nCash on cash ROI: {final*100}%')

prop1 = RoiCalc()
prop1.run()