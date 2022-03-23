#
# ps7pr5.py (Problem Set 7, Problem 5)
#
# TT Securities
#
#  Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """

    print('Day Price')
    print('--- -----')
    if prices == []:
        return 0, 0.0
    else:
        for i in range(len(prices)):
            print('%3.0f' % i, '%5.2f' % prices[i])



def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]



def average_price(prices):
    """ returns the average of a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    result = 0
    for i in prices:
        result += i
    result = result / len(prices)
    return result


def standard_deviation(prices):
    """ returns the standard deviation of a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    result1 = 0
    result2 = 0
    average = average_price(prices)
    for i in prices:
        result1 = (i - average)**2
        result2 += result1
    print('The standard deviation is', ((result2 / len(prices))**(1/2)))

def max_price(prices):
    """ returns the maximum price, and the day of the max price, in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    m = prices[0]
    day = 0
    for x in prices:
        if x > m:
            m = x
    for i in range(len(prices)):
        if prices[i] == m:
            day = i
    print('The maximum price is', m, 'on day', day)

        
def threshold(prices):
    """ returns the number of prices below a certain threshold.
        input: a threshold and a list of 1 or more numbers.
    """
    threshold = int(input('Enter the threshold: '))
    print()
    result= 0
    
    for x in prices:
        if x < threshold:
            result += 1
    if result > 0:
        if result == 1:
            print('There is at least one price under', threshold)
        else:
            print('There are at least', result, 'prices under', threshold)
    else:
        print('There are no prices under', threshold)
            

def investment(prices):
    """ returns a plan that results in the largest profit.
        input: prices is a list of 1 or more numbers.
    """
    day1 = 0
    day2 = 0
    buy = 0
    sell = 0
    best = 0
    result = []
    z = 0

    # first determine the largest profit based upon the order of days
    for i in range(len(prices)):
        for j in range(len(prices)):
            if j > i:
                day1 = i
                day2 = j
                buy = prices[i]
                sell = prices[j]
                best = sell - buy
                if [best] > result:
                    result += [best]

    #finds the max total profit
    plan = max(result)

    # then redefine the variables buy, sell, day1 and day2 to fit the
    # max profit found
    
    for x in prices:
        for y in prices:
            z = y - x
            if z == plan:
                buy = x
                sell = y
    for i in range(len(prices)):
        if prices[i] == buy:
            day1 = i
    for j in range(len(prices)):
        if prices[j] == sell:
            day2 = j
    
    print('Buy on day', day1, 'at price', buy)
    print('Sell on day', day2, 'at price', sell)
    print('Total profit:', plan)
    
            
def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice == 3:
            average = average_price(prices)
            print('The average price is', average)
        elif choice == 4:
            standard_deviation(prices)
        elif choice == 5:
            max_price(prices)
        elif choice == 6:
            threshold(prices)
        elif choice == 7:
            investment(prices)
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')


