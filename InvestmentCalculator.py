#Investment per year, percentage profits per year, years invested
investment = 1000000
percentageIncrease = 10
years = 31

def calcInvest(year):
    net = 0
    percent = percentageIncrease/100 +1
    for x in range(year):
        net+= investment
        net = net*percent
    profit = net - (investment*year)
    gain = net/(investment*year)*100 -100
    inflation = net*.98**year
    gain = "{:,.2f}%".format(gain)
    profit = "${:,.2f}".format(profit)
    net = "${:,.2f}".format(net)
    inflation = "${:,.2f}".format(inflation)
    return 'Net Worth: ' + net +'\nProfit: ' + profit + '\nGain: ' + gain + '\nInflation: ' + inflation 
print(calcInvest(years))