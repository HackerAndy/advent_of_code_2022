import os
import numpy

one_through_one_hundred = list(range(1,101))

def part1():
    num_of_full_overlaps = 0
    num_of_partial_overlaps = 0

    data_file = open(data_file_name, 'r')
    # the_data = data_file.read().splitlines()
    data_array = numpy.genfromtxt(data_file, delimiter=",", dtype="str")
    # print(data_array)
    for assignment_pairs in data_array:
        group1_assignment = assignment_pairs[0].split("-")
        group2_assignment = assignment_pairs[1].split("-")
        group1_start = int(group1_assignment[0])
        group1_end = int(group1_assignment[1])
        group2_start = int(group2_assignment[0])
        group2_end = int(group2_assignment[1])
        # print("Group1 start:", group1_start, "end:", group1_end)
        # print("Group2 start:", group2_start, "end:", group2_end)
        group1_assignments_as_list = one_through_one_hundred[group1_start-1:group1_end]
        group2_assignments_as_list = one_through_one_hundred[group2_start-1:group2_end]
        # print("G1 assignments:", group1_assignments_as_list, "G2 assignments", group2_assignments_as_list)

        number_of_assignments_g1 = len(group1_assignments_as_list)
        number_of_assignments_g2 = len(group2_assignments_as_list)

        # print("Num of assignments:", number_of_assignments)

        overlapped_assignments = set(group1_assignments_as_list).intersection(group2_assignments_as_list)

        if len(overlapped_assignments) == number_of_assignments_g1:
            num_of_full_overlaps += 1
        elif len(overlapped_assignments) == number_of_assignments_g2:
            num_of_full_overlaps += 1

        if len(overlapped_assignments) > 0:
            num_of_partial_overlaps += 1

    print("Number of full overlaps:", num_of_full_overlaps)
    print("Number of partial overlaps:", num_of_partial_overlaps)

data_file_name = 'data/data'
part1()
