def is_pivot_index(current_word, previous_word):
    """Return a boolean indicating whether the current word is 
    ordered before the previous word, i.e. if the current word 
    is the rotation point.
    """
    if current_word < previous_word:
        return True
    else:
        return False
    
def brute_force_one(words):
    """Returns the index of the 'rotation point'.
    Time complexity: O(n)
    Space complexity: O(1)
     """
    if is_pivot_index(words[0], words[-1]):
        print(i, words[i])
        return i
    else:
        number_of_words = len(words)
        for i in range(1, number_of_words):
            if is_pivot_index(words[i], words[i-1]):
                print(i, words[i])
                return i
                break

def binary_search(words):
    """Returns the index of the 'rotation point'.
    Time complexity: O(logn)
    Space complexity: O(1)
    """
    if is_pivot_index(words[0], words[-1]):
        print(i, words[i])
        return i
    else:
        # Binary tree to speed things up.
        floor_index = 0
        ceiling_index = len(words)
        
        # Todo: Check if int ruins alg
        found_pivot = False
        while found_pivot = False:
            halfway_distance = int((ceiling_index - floor_index)/2)
            current_index = floor_index + halfway_distance
            floor_word = word[floor_index]
            current_word = word[current_index]
            if prev_word > current_word:
                # Then rotation point is in first half of current interval

                # Check if current word is rotation point
                if is_pivot_index(current_word, words[current - 1]):
                    # If it is, we are done.
                    found_pivot = True
                    return current

                else:
                    # Reset the distance 
                    ceiling_index = current_index
                    current_temp = current
                    current = current - (current - prev) / 2
                    prev = current_temp
            else:
                # Pivot is in second half of current interval
                floor_index = current_index

        # Get index of the first lettor of the first word, init_index
        # Get the index of the first letter of the middle word
        # Do is_pivot_index
        # If
        # 

# Test case
words_one = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print(brute_force_one(words_one))