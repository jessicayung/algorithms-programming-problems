"""
InterviewCake Problem 4

Let's work with two tuples at a time, e.g. (3,5) and (4,8).
There is overlap (i.e. they should merge if
(1) tuple_one[0] <= tuple_two[0] and tuple_one[1] >= tuple_two[0]
                  or the other way round (switch tuples 1,2)
Can take a greedy approach -> merge as we go.

...
Insight: if you don't merge with any tuples the first run through, you will NEVER merge with any of the tuples.
So we should compare the first tuple with every other tuple. And then we can throw it away.

>>> condense_meeting_times_alt([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
[(0, 1), (3, 8), (9, 12)]


"""


def condense_meeting_times_alt(meeting_times):
    sorted_meeting_times = sorted(meeting_times)
    merged_meetings = [meeting_times[0]]

    for current_meeting_start, current_meeting_end in sorted_meeting_times[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        # If current and last_merged_meeting overlap:
        if current_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        # Else add current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))
    return merged_meetings


def merge(first, second):
    return first[0], second[1]


def condense_meeting_times(list_of_tuples):
    """Rubbish."""
    new_list_of_tuples = []
    index = 0
    list_len = len(list_of_tuples)
    action_two_tuples(list_of_tuples[0], list_of_tuples[1], list_of_tuples)
    while index + 1 < list_len:
        for j in range(index + 1, list_len):
            action_two_tuples(list_of_tuples[index], list_of_tuples[j], new_list_of_tuples)


def action_two_tuples(first_index, second_index, tuples_list):
    """Also rubbish."""
    first = tuples_list[first_index]
    second = tuples_list[second_index]
    if first[0] <= second[0]:
        if first[1] >= second[0]:
            # TODO: list append merged times properly
            tuples_list.append(merge(first_index, second_index))
            # TODO: delete(first, second)
    else:
        # i.e. we know first[0] > second[0]
        if second[1] >= first[0]:
            # TODO: list append merged, delete prev
            merge(second_index, first_index)
