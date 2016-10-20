import unittest

def get_max_profit(stock_prices_yesterday):
    """Uses greedy approach. A greedy algorithm iterates through the problem space taking the optimal solution "so far,"
     until it reaches the end.

    The greedy approach is only optimal if the problem has "optimal substructure," which means stitching together
    optimal solutions to sub-problems yields an optimal solution.
    """
    if len(stock_prices_yesterday) < 2:
        raise IndexError("Getting a profit requires at least 2 prices.")
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    for index, price in enumerate(stock_prices_yesterday):
        if index == 0:
            continue
        current_price = price
        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)
    return max_profit

def get_product_of_all_ints_except_at_index(int_list):
    # Create list
    products = [None] * len(int_list)
    print(products)
    cum_product = int_list[0]
    print("First int: ", cum_product)
    products[0] = 1
    # Product of all numbers before int
    for i in range(1, len(int_list)):
        print("before: ", i, cum_product)
        products[i] = cum_product
        cum_product *= int_list[i]
    # Product of all numbers after int
    after_product = int_list[-1]
    for j in range(2,len(int_list)+1):
        print("after: ", len(int_list)+1-j, after_product)
        products[-j] *= after_product
        after_product *= int_list[-j]
    print(products)
    return products


def my_function(arg):
    # write the body of your function here
    return 'running with %s' % arg


# run your function through some test cases here
# remember: debugging is half the battle!
print
my_function('test input')


def product(list_of_ints):
    pass


def max_three(list_of_ints):
    pass


def min_three(list_of_ints):
    pass


def highest_product_from_list_of_ints(list_of_ints):
    if len(list_of_ints) == 3:
        return product(list_of_ints)
    elif min(list_of_ints) >= 0:
        return product(max_three(list_of_ints))
    elif max(list_of_ints) <= 0:
        return product(min_three(list_of_ints))
    # If some are positive and some are negative
    else:
        sorted_list_of_ints = sorted(list_of_ints)

        max_1 = max(list_of_ints)
        max_2 = second_max(list_of_ints)
        min_1 = min(list_of_ints)
        # min_2 =


class Tests(unittest.TestCase):
    def test_p2_get_product_of_all_ints_except_at_index(self):
        numbers = [1,2,3]
        self.assertEqual(get_product_of_all_ints_except_at_index(numbers), [6,3,2])

if __name__ == '__main__':
    unittest.main()