#Investment per year, percentage profits per year, years invested
investment = 40000
percentageIncrease = 50
years = 5

def calcInvest(year):
    net = 0
    percent = percentageIncrease/100 +1
    for x in range(year):
        net+= investment
        net = net*percent
    profit = net - (investment*year)
    gain = net/(investment*year)*100 -100
    gain = "{:,.2f}%".format(gain)
    profit = "${:,.2f}".format(profit)
    net = "${:,.2f}".format(net)
    return 'Net Worth: ' + net +'\nProfit: ' + profit + '\nGain: ' + gain
print(calcInvest(years))