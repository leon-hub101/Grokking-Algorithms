function binarySearch1(arr, item) {
    let low = 0;
    let high = arr.length - 1;
    
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let guess = arr[mid];

        if (guess === item) {
            return mid;
        }
        if (guess > item) {
            high = mid - 1;
         } else {
            low = mid + 1;
         }
    }
    return -1
}

const my_nums_list = [
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

const names = [
    "Olivia", "Noah", "Emma", "Liam", "Sophia", "Jacob", "Ava", "Mason", "Isabella", "William",
    "Mia", "Ethan", "Amelia", "James", "Harper", "Alexander", "Emily", "Michael", "Charlotte", "Benjamin",
    "Madison", "Elijah", "Abigail", "Daniel", "Lily", "Aiden", "Chloe", "Logan", "Grace", "Matthew",
    "Victoria", "Lucas", "Aria", "Jackson", "Scarlett", "David", "Zoe", "Carter", "Layla", "Jayden",
    "Ellie", "John", "Nora", "Owen", "Evelyn", "Dylan", "Lucy", "Luke", "Anna", "Henry"
]

const sortedNames = names.sort();


const test1 = binarySearch1(my_nums_list, 123);
console.log(test1);

function binarySearch2(arr, item) {
    let low = 0;
    let high = arr.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let guess = arr[mid];

        if (guess === item) {
            return mid;
        }
        if (guess > item) {
            high = mid - 1;
         } else {
            low = mid + 1;
         }
    }
    return -1
}

const test2 = binarySearch2(sortedNames, "Scarlett");
console.log(test2);

function binarySearch3(arr, item) {
    let low = 0;
    let high = arr.length -1

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let guess = arr[mid];

        if (guess === item) {
            return mid;
        } 
        
        if (guess > item) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    } 
    return -1;
}

const test3 = binarySearch3(sortedNames, "Elijah");
console.log(test3);