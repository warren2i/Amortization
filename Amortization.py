principalbal=[]
interestarr=[]
totalinterestarr=[]
totalpaymentarr=[]
principal=[]
totalinterest=0
totalpayment=0

print("how much do you wish to borrow?")
while True:
    try:
        loanammount=int(input())
    except ValueError:
        print('data is not int')
        #better try again... Return to the start of the loop
        continue
    else:
        break
print("What is the interest rate, in decimal form?")
while True:
    try:
        interest=float(input())
    except ValueError:
        print('data is not float')
        #better try again... Return to the start of the loop
        continue
    else:
        break
print("What is the length of the term in months?")

while True:
    try:
        months=int(input())
    except ValueError:
        print('data is not int')
        #better try again... Return to the start of the loop
        continue
    else:
        break

def amortization(loanammount, interest, months):
    xd = loanammount * (((interest / 12) * ((interest / 12 + 1) / months)) / ((interest / 12 + 1) / months) - 1)
    return round((loanammount + xd), 2)


def amortizationammount(loanammount, interest, months):
    montlyinterest = interest / 12
    montlypayment = loanammount * (
            montlyinterest * (pow((1 + montlyinterest), (months))) / (pow((1 + montlyinterest), (months)) - 1))
    return round(montlypayment, 2)


def calcs(loanammount, interest, months):
    totalpaymentdue = round(amortizationammount(loanammount, interest, months), 2)
    computedinterestdue = round((amortization(loanammount, interest, months)), 2)
    principaldue = round(
        (amortizationammount(loanammount, interest, months)) - (amortization(loanammount, interest, months)), 2)
    principlebalance = round((loanammount - principaldue), 2)
    return principlebalance, totalpaymentdue, computedinterestdue, principaldue, months

def amortization_tabulate(loanammount, interest, months):
    newammount = loanammount
    for month in range(months):
        newammount, totalpaymentdue, computedinterestdue, principaldue, period = calcs(newammount, interest,(months - month))
        principalbal.append(newammount)
        global monthlypayment
        monthlypayment = totalpaymentdue
        global totalinterest
        global totalpayment
        totalinterest = totalinterest + computedinterestdue
        interestarr.append(computedinterestdue)
        totalinterestarr.append(totalinterest)
        totalpayment = totalpayment + totalpaymentdue
        totalpaymentarr.append(totalpayment)
        principal.append(principaldue)
    return (principal, interestarr, principalbal)

def totalloancost(loanammount, interest, months):
    totalcost = (amortizationammount(loanammount, interest, months)) * months
    return round(totalcost, 2)


def interestcost(loanammount, interest, months):
    totalcost = (amortizationammount(loanammount, interest, months)) * months - loanammount
    return round(totalcost, 2)

def run_calcs(loan_ammount,interest,months):
    a = amortization(loan_ammount,interest,months)

    b=amortizationammount(loan_ammount,interest,months)

    principal, interestarr, principalbal = amortization_tabulate(loan_ammount,interest,months)


    e = totalloancost(loan_ammount,interest,months)

    f = interestcost(loan_ammount,interest,months)
    montharr = [m + 1 for m in range(months)]
    return montharr,months,interest,loan_ammount,a,b,principal,interestarr,principalbal,e,f


def linechart():
    with open('html/js/line_chart_temp.js', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('{months}', str(montharr))
    filedata = filedata.replace('{data_1}', str(totalpaymentarr))
    filedata = filedata.replace('{data_1}', str(totalpaymentarr))
    filedata = filedata.replace('{data_2}', str(totalinterestarr))
    filedata = filedata.replace('{data_3}', str(principalbal))
    filedata = filedata.replace('{pie_1}', str(totalinterestarr[0]))
    filedata = filedata.replace('{pie_2}', str(loan_ammount))
    with open('html/js/line_chart.js', 'w') as file:
        file.write(filedata)
def pie_chart():
    with open('html/js/pie_chart_temp.js', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('{interest}', str(totalloancost))
    filedata = filedata.replace('{principal}', str(interestcost))
    with open('html/js/pie_chart.js', 'w') as file:
        file.write(filedata)

def table(*args, **headers):
    zipped = list(zip(*args))
    html = '<table class="table table-dark table-hover table-responsive">'
    html = html + ('<thead>')
    html = html + ('<tr>')
    if not headers:
        pass
    else:
        for head in headers["headers"]:
            html = html + (f'<th scope="col">{head}</th>')
        html = html + ('</tr>')
        html = html + ('</thead>')
    html = html + ('<tbody>')
    for x in zipped:
        html = html + '<tr>'
        for y in x:
            html = html + (f"<td>{y}</td>")
        html = html + '</tr>'
    html = html + '</tbody>'
    html = html + '</table>'
    return html

def tables():
    with open('html/chart_temp.html', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('{table}', htmldata)
    filedata = filedata.replace('{term_length}', str(months))
    filedata = filedata.replace('{borrowed_ammount}', str(loan_ammount))
    filedata = filedata.replace('{total_cost}', str(loan_ammount + totalinterest))
    filedata = filedata.replace('{interest_cost}', str(totalinterest))
    filedata = filedata.replace('{monthly_payment}', str(monthlypayment))
    with open('html/chart.html', 'w') as file:
        file.write(filedata)

montharr,months,interest,loan_ammount,amortization,amortizationammount,principal,interestarr,principalbal,totalloancost,interestcost = run_calcs(loanammount,interest,months)

linechart()
pie_chart()
htmldata = (table(montharr, principal, interestarr, principalbal,
                  headers = ("Months", "Principal", "Interest", "Principal Balance")))
tables()

