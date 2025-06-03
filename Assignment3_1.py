def find_max_sum(tups_list):
    max_sum = float('-inf')
    max_tuple = None

    for tpl in tups_list:
        current_sum = sum(tpl)
        if current_sum > max_sum:
            max_sum = current_sum
            max_tup = tpl

    return max_tup, max_sum

def find_tups_with_n_digits(tups_list, n):
    result = []

    for tpl in tups_list:
        for num in tpl:
            if 10 ** (n - 1) <= abs(num) < 10 ** n:
                result.append(tpl)
                break

    return result

list_of_tups = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 20, 30)]
n = int(input("Enter the value of N (1, 2, or 3): "))

max_tup, max_sum = find_max_sum(list_of_tups)
print(f"The tuple with the max sum is {max_tup}, sum of {max_sum}")

tups_with_n_digits = find_tups_with_n_digits(list_of_tups, n)
print(f"Tuples with at least one number with {n} digits: {tups_with_n_digits}")