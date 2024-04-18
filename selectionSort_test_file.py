def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr) 
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

"""
The two functions provided are examples of implementing the **Selection Sort** algorithm in Python. 
Below is an explanation of each function and how they work together to sort an array:

Function `findSmallest(arr)`
This function is designed to find the index of the smallest element in the array `arr`.

1. Initialization:
   - `smallest` is initialized to the first element of the array (`arr[0]`), and `smallest_index` is set to `0`. 
   These variables keep track of the smallest value found and its index as the function iterates through the array.

2. Iteration:
   - The function iterates through the array starting from the second element (`range(1, len(arr))`), since the first element is already assumed to be the smallest initially.
   
3. Comparison:
   - During each iteration, it compares the current element (`arr[i]`) with the value of `smallest`.
   - If a smaller element is found (`arr[i] < smallest`), `smallest` is updated to this new lower value, and `smallest_index` is updated to the current index (`i`).

4. Result:
   - After iterating through the list, the function returns `smallest_index`, which is the index of the smallest element in the array.

Function `selectionSort(arr)`
This function implements the selection sort algorithm, which sorts an array by repeatedly finding the smallest element from the unsorted part and moving it to the beginning.

1. Initialization:
   - `newArr` is initialized as an empty list that will eventually contain the sorted elements.
   - `copiedArr` is a copy of the original array `arr`. This is necessary to avoid modifying the original array while elements are being removed during the sorting process.

2. Sorting Process:
   - The function uses a loop that iterates over the length of `copiedArr`.
   - In each iteration, it calls `findSmallest(copiedArr)` to find the index of the smallest element in the current list.
   - It then appends this smallest element to `newArr` and removes it from `copiedArr` using `pop(smallest)`. 
   The `pop` method removes the item at the specified index and returns it, which is why it is immediately appended to `newArr`.

3. Completion:
   - The loop continues until all elements have been removed from `copiedArr` and appended to `newArr` in sorted order.
   - The function finally returns `newArr`, which now contains all the elements from the original array, sorted in ascending order.

Conclusion
The `selectionSort` function effectively sorts any list of numbers in ascending order by repeatedly extracting the smallest element and adding it to a new list. 
This method is simple to understand and implement but is not the most efficient for large datasets due to its \(O(n^2)\) time complexity, where \(n\) is the number of elements in the list.
"""

names = [
    "Olivia", "Noah", "Emma", "Liam", "Sophia", "Jacob", "Ava", "Mason", "Isabella", "William",
    "Mia", "Ethan", "Amelia", "James", "Harper", "Alexander", "Emily", "Michael", "Charlotte", "Benjamin",
    "Madison", "Elijah", "Abigail", "Daniel", "Lily", "Aiden", "Chloe", "Logan", "Grace", "Matthew",
    "Victoria", "Lucas", "Aria", "Jackson", "Scarlett", "David", "Zoe", "Carter", "Layla", "Jayden",
    "Ellie", "John", "Nora", "Owen", "Evelyn", "Dylan", "Lucy", "Luke", "Anna", "Henry",
    "Elizabeth", "Gabriel", "Levi", "Brooklyn", "Samuel", "Addison", "Joseph", "Ella", "Joshua", "Aubrey",
    "Andrew", "Lillian", "Ryan", "Natalie", "Cameron", "Luna", "Hunter", "Savannah", "Jack", "Penelope",
    "Christian", "Violet", "Wyatt", "Stella", "Jonathan", "Hazel", "Christopher", "Aurora", "Jaxon", "Zoey",
    "Julian", "Riley", "Aaron", "Emilia", "Charles", "Paisley", "Thomas", "Audrey", "Isaac", "Skylar",
    "Caleb", "Peyton", "Nathan", "Serenity", "Connor", "Ariana", "Jeremiah", "Genesis", "Sebastian", "Piper"
]

unsorted_numbers = [
    39797685, 43039264, 45555483, 84109462, 33371926, 2294103, 48028269, 91794594, 21115118, 96431266,
    63647557, 59794447, 16820874, 46159779, 69844573, 63317887, 63401369, 6334479, 16981399, 55078324,
    69739059, 26721644, 33292374, 87187322, 25782265, 24756653, 76929730, 3754830, 30629260, 89336202,
    2454819, 13286036, 82398055, 44420263, 47091380, 8469754, 63200945, 64006393, 46640912, 76335646,
    77447085, 24058957, 71051401, 69580136, 71344370, 36431512, 27030068, 17075901, 84843921, 41674252,
    24294011, 57641190, 48304694, 68242555, 49923638, 4984581, 86000453, 88048339, 85718378, 84651093,
    86150391, 76335176, 60091195, 12098278, 20442963, 4598088, 62304269, 35627649, 9851495, 14490245,
    34453719, 50404776, 89555175, 88353689, 28561467, 38110674, 21171286, 49166500, 89368578, 12296993,
    68683605, 86282459, 23443466, 69135008, 65688622, 66696446, 12831703, 28092591, 54520428, 9573822,
    46587372, 30254612, 62060452, 16728950, 83152241, 68263017, 32156261, 63448075, 81274538, 88797459
]


print(selectionSort(names))
print(selectionSort(unsorted_numbers))