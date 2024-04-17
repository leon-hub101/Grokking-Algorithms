def binary_search(arr, item):
    # Low and High keep track of which part of the list you're searching in
    low = 0
    high = len(arr) - 1

    while low <= high: # While you haven't narrowed it down to one element
        mid = (low + high) // 2 # Check the middle element
        guess = arr[mid]
        if guess == item: # If item was found, return it
            return mid
        elif guess > item: # If the guess was more than the item index, set high to mid - 1
            high = mid - 1
        else: # If the guess was less than the item index, set low to mid + 1
            low = mid + 1
    return None # Return None if the item wasn't found

def sort_list(list):
    return sorted(list)

unsorted_names_list = [
    "Olivia", "Noah", "Emma", "Liam", "Sophia", "Jacob", "Ava", "Mason", "Isabella", "William",
    "Mia", "Ethan", "Amelia", "James", "Harper", "Alexander", "Emily", "Michael", "Charlotte", "Benjamin",
    "Madison", "Elijah", "Abigail", "Daniel", "Lily", "Aiden", "Chloe", "Logan", "Grace", "Matthew",
    "Victoria", "Lucas", "Aria", "Jackson", "Scarlett", "David", "Zoe", "Carter", "Layla", "Jayden",
    "Ellie", "John", "Nora", "Owen", "Evelyn", "Dylan", "Lucy", "Luke", "Anna", "Henry"
]

my_nums_list = [
    1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
    21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
    41, 43, 45, 47, 49, 51, 53, 55, 57, 59,
    61, 63, 65, 67, 69, 71, 73, 75, 77, 79,
    81, 83, 85, 87, 89, 91, 93, 95, 97, 99,
    101, 103, 105, 107, 109, 111, 113, 115, 117, 119,
    121, 123, 125, 127, 129, 131, 133, 135, 137, 139,
    141, 143, 145, 147, 149, 151, 153, 155, 157, 159,
    161, 163, 165, 167, 169, 171, 173, 175, 177, 179,
    181, 183, 185, 187, 189, 191, 193, 195, 197, 199
]

sorted_names_list = sort_list(unsorted_names_list)
print(sorted_names_list)

mia = binary_search(sorted_names_list, "Mia")
print(mia)

my_num = binary_search(my_nums_list, 157)
print(my_num)

