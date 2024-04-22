function findSmallest(arr) {
    let smallest = arr[0];
    let smallestIndex = 0;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
            smallestIndex = i;
        }
    }
    return smallestIndex;
}

function selectionSort(arr) {
    newArr = [];
    copiedArr = arr.slice();
    while (copiedArr.length > 0) {
        let smallestIndex = findSmallest(copiedArr);
        newArr.push(copiedArr.splice(smallestIndex, 1)[0]);
    }
    return newArr;
}

const names = [
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

const unsorted_numbers = [
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

sorted_names = selectionSort(names);
smallest_num = findSmallest(unsorted_numbers);
sorted_num_list = selectionSort(unsorted_numbers);

console.log("JavaScript sorted Names list: ", sorted_names);
console.log("JavaSript smallest number from list: ", smallest_num);
console.log("JavaSript sorted numbers list: ", sorted_num_list);