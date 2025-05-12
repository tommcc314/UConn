def price_to_profit(L):
    profit = []
    for i in range(len(L)):
        #first change is always 0
        if i == 0:
            profit.append(0)
        #take difference of current day and previous day
        else:
            profit.append(L[i] - L[i - 1])
    return profit

# brute force solution, for reference
def max_profit_brute(L):
    n = len(L)
    max_sum = 0

    # outer loop finds the max profit for each buy day
    for i in range(n):
        total = 0

        # inner loop finds the profit for each sell day
        for j in range(i+1, n):
            total += L[j] # total profit if we sell on day j
            if total > max_sum: max_sum = total

    return max_sum

def max_profit(L):
    def search_profit(L, left, right):
        #base case: return profit
        if left == right:
            return L[left]
        center = (left + right) // 2
        #divide and conquer
        return max(search_profit(L, left, center), search_profit(L, center + 1, right), _max_profit_center(L, left, right, center))
    return search_profit(L, 0, len(L) - 1)

def _max_profit_center(L, left, right, med):
    #find best buy price to the left
    buy_price = 0
    best_buy = 0
    for i in range(med, left, -1):
        buy_price += L[i]
        if buy_price > best_buy:
            best_buy = buy_price
    # find maximum profit when buy on median
    sell_price = 0
    max_sell = 0
    for i in range(med + 1, right + 1):
        sell_price += L[i]
        if sell_price > max_sell:
            max_sell = sell_price
    return max(best_buy, max_sell, (best_buy + max_sell))

    # time complexity of algorithm is O(n)

# some test cases, and an example of reading CSVs
if __name__ == '__main__':
    # some basic tests of the necessary functions
    assert price_to_profit([100, 105, 97, 200, 150]) == [0, 5, -8, 103, -50]
    assert max_profit([0, 5, -8, 103, -50]) == 103
    assert max_profit([0, -1, 3, 4, -5, 9, -2]) == 11

    ##### Import and read values from associated csvs, then check if you can become a bitcoin-optimaire
    import csv
    import os


    val_2015 = []
    val_2016 = []
    val_2017 = []
    val_2018 = []
    val_2019 = []
    val_2020 = []

    vals = [val_2015, val_2016, val_2017, val_2018, val_2019, val_2020]

    for file in os.scandir(r'./bitcoin_prices'):
        if (file.path.endswith(".csv")):
            if file.name == "2015.csv": i = 0
            elif file.name == "2016.csv": i = 1
            elif file.name == "2017.csv": i = 2
            elif file.name == "2018.csv": i = 3
            elif file.name == "2019.csv": i = 4
            elif file.name == "2020.csv": i = 5

            with open(file, 'r') as f:
                reader = csv.reader(f)

                lst = list(reader)[1:]
                for j in range(len(lst)):
                    vals[i].append( float(lst[j][1].replace(",","")))


     # find the profits for each year
    year_profits = []
    for year in vals:
        year_profits.append([])
        year_profits[-1] = price_to_profit(year)

    # correct max profits per year, 2015-2020, rounded to ints
    max_profits = [298, 604, 18561, 4476, 9665, 24052]

    # test that max_profit returns the correct profit for each year
    # test time taken for brute force and divide & conquer
    for i, year in enumerate(year_profits):
        assert round(max_profit(year), 0) == max_profits[i]
