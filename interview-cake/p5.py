"""
Problem 5

Also covers:
- Memo-ization (Fibonacci numbers example)


"""


def combinations(amount, denominations):
    sorted_denoms = sorted(denominations)
    combos = 0
    if sorted_denoms[0] > amount:
        return combos
    if divmod(amount, denominations[0])[1] == 0:
        pass
    """
    for multiples in range(divmod(amount, min)[0])
    Try divmod(amount, min)[0] min.

    if divmod(amount, min)[1] == 0:
        combos += 1
        # Then Try divmod(amount, min)[0] -2

    Try (#smallest you can fit - 2) smallest + 1 second smallest
        if too small, try + 1 third smallest... until greater than or equal to
        if equal,
    Try (#smallest
    """


number_of_ways = 0


def num_ways_top_down(amount, denominations, current_index=0,):

    # Previously got to exact amount
    if amount == 0:
        return 1
    # Overshot: Used too many coins
    if amount < 0:
        return 0
    # Used all denominations, so no remaining ways to resolve
    if current_index == len(denominations):
        return 0

    # Choose a current denomination (using current_index)
    current_denomination = denominations[current_index]

    num_possibilities = 0
    while amount >= 0:
        num_possibilities += num_ways_top_down(amount, denominations, current_index+1)
        amount -= current_denomination

    for denomination in denominations:
        # for each number_of_times_to_use_denomination in possible_number_of_times_to_use_denom_without_overshooting_amount:
        for times_to_use in range(divmod(amount, denomination)[0]):
            number_of_ways += num_ways(remaining_amount, denominations)

    # Might there not be double counting?


