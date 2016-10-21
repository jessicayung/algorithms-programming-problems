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
    for j in range(2, len(int_list)+1):
        print("after: ", len(int_list)+1-j, after_product)
        products[-j] *= after_product
        after_product *= int_list[-j]
    print(products)
    return products


def product(list_of_ints):
    return list_of_ints[0] * list_of_ints[1] * list_of_ints[2]


def max_three(list_of_ints):
    sorted_list_of_ints = sorted(list_of_ints)
    return sorted_list_of_ints[:3]


def min_three(list_of_ints):
    sorted_list_of_ints = sorted(list_of_ints)
    return sorted_list_of_ints[-3:]


def highest_product_from_list_of_ints(list_of_ints):
    if len(list_of_ints) == 3:
        return product(list_of_ints)
    elif min(list_of_ints) >= 0:
        return product(max_three(list_of_ints))
    elif max(list_of_ints) <= 0:
        return product(min_three(list_of_ints))
    # If some are positive and some are negative
    else:
        # Sort in ascending order
        sorted_list_of_ints = sorted(list_of_ints)
        # We want one positive and
        # two neg or two pos, depending on which product is larger.
        if sorted_list_of_ints[1] < 0 or sorted_list_of_ints[-3] > 0:
            max_1 = sorted_list_of_ints[-1]
            max_pos = sorted_list_of_ints[-2] * sorted_list_of_ints[-3]
            max_neg = sorted_list_of_ints[0] * sorted_list_of_ints[1]
            max_2_3 = max(max_pos, max_neg)
            if max_2_3 > 0:
                return max_1 * max_2_3
        elif 0 in list_of_ints:
            return 0
        else:
            # The remaining alternative: Product is negative.
            # Precisely one negative number, two positive numbers and no zeroes.
            # That means we have precisely three integers. This case was covered.
            return "Error"

def highest_product_from_list_of_ints_greedy(list_of_ints):
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    if list_of_ints[3] is None:
        return highest_product_of_three
    highest = list_of_ints[0]
    lowest = list_of_ints[0]
    max_product_two = list_of_ints[0] * list_of_ints[1]
    min_product_two = list_of_ints[0] * list_of_ints[1]
    # Go through list
    for int in list_of_ints:
        highest_product_of_three = max(int * highest, int * min_product_two, highest_product_of_three)
        max_product_two = max(highest*int, lowest*int, max_product_two)
        min_product_two = min(lowest*int, lowest*int, min_product_two)
        highest = max(highest, int)
        lowest = min(lowest, int)
    return highest_product_of_three

    # LOGIC:
    # PPP -> max*max_product_two
    # PPN -> min*max_product_two
    # PNN -> min*min_product_two
    # NNN -> max*min_product_two
    # NN...0 or PPN0 -> the 0 kicks in during highest_product_of_three = max(...)

class Tests(unittest.TestCase):
    def test_p2_get_product_of_all_ints_except_at_index(self):
        numbers = [1, 2, 3]
        self.assertEqual(get_product_of_all_ints_except_at_index(numbers), [6, 3, 2])

    def test_highest_product_from_list_of_ints(self):
        self.assertEqual(highest_product_from_list_of_ints([10, 2, 0, 3, -5]), 60)
        self.assertEqual(highest_product_from_list_of_ints([1000, 2, 0, -100]), 0)
        self.assertEqual(highest_product_from_list_of_ints([-10, -5, 1, 2, 3, 4]), 200)
        self.assertEqual(highest_product_from_list_of_ints([-10, -10, 1, 3, 2]), 300)

if __name__ == '__main__':
    unittest.main()
