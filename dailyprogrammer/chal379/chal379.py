#DONE, could make overall function more efficient

#https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/

# income 10,000 -> tax 0.0
# income 30,000 -> tax 0.1
# income 100,000 -> tax 0.25
# income >100k -> tax 0.4

# class used to store the tax rates and call the functions
class TaxRates:
    def __init__(self, rates):
        self.rates = rates

    #finds the tax amount for a given amount based on the rates stored in the object
    def getTaxAmt(self, amount):
        taxAmt = 0
        income = amount
        rates = self.rates

        i = len(rates) - 1
        while(i > 0):
            if income > rates[i-1][0]:
                income -= rates[i-1][0]
                taxAmt += income*rates[i][1]
                income = rates[i-1][0]
            i -= 1

        return int(taxAmt)

    #finds the first income that matches the percent taxed
    # returns -1 if the number is not possible, or the actual number
    # rounds percent to hundredths place, so it is not exact percentage
    # function is inefficient (possible fix, binary search)
    def getOverall(self, percent):
        bool = 0
        income = 0
        if percent >= self.rates[-1][1]:
            return -1
        while(bool == 0):
            taxAmt = self.getTaxAmt(income)
            if income != 0:
                if percent == round(taxAmt/income, 2):
                    return income
            else:
                if percent == 0:
                    return 0
            income += 1

# function to get info from file
#   stores as a 2D array of [int, float], represents [income amount, percentage amount]
def getFromFile(filename):
    ratesList = []
    with open(filename, "r") as f:
        data = f.read()
    rates = data.replace(" ", "").split("\n")
    ratesList = [i.split(",") for i in rates if i]
    for i in range(len(ratesList)):
        if ratesList[i][0] != "--":
            ratesList[i][0] = int(ratesList[i][0])
        ratesList[i][1] = float(ratesList[i][1])
    #print(ratesList)
    return ratesList


# NO LONGER USED
# this function does not make it easy to do more than 4, will change to allow for that
# function to calc amount for tax
def getTaxDollars(income):
    taxAmt = 0
    if income <= 10000:
        taxAmt = 0
    elif income <= 30000:
        taxAmt = (income-10000)*0.1
    elif income <= 100000:
        taxAmt = (20000*0.1) + (income-30000)*0.25
    else:
        taxAmt = (20000*0.1) + (70000*0.25) + (income-100000)*0.4

    return int(taxAmt)


###  main test
#print(getTaxDollars(0))
#print(getTaxDollars(10000))
#print(getTaxDollars(10009))
#print(getTaxDollars(10010))
#print(getTaxDollars(12000))
#print(getTaxDollars(56789))
#print(getTaxDollars(1234567))

#file test (before return)
#getFromFile("input.txt")

#object test
test = TaxRates(getFromFile("input.txt"))
print(test.rates)
print("-----------------")

print(test.getTaxAmt(0))
print(test.getTaxAmt(10000))
print(test.getTaxAmt(10009))
print(test.getTaxAmt(10010))
print(test.getTaxAmt(12000))
print(test.getTaxAmt(56789))
print(test.getTaxAmt(1234567))
print("-----------------")

print(test.getOverall(0.00))
print(test.getOverall(0.06))
print(test.getOverall(0.09))
print(test.getOverall(0.32))
print(test.getOverall(0.40))
print(test.getOverall(0.50))

# optional:
#   bring in rates from file [DONE]
#   use the percentage taxed to determine the income of a person
    # [DONE, has different numbers due to rounding]
