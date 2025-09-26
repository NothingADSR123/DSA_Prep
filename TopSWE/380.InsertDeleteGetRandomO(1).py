# Implement the RandomizedSet class:
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

# Example 1:
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

# Obviously ok approach But it seems remove function takes O(n) time so to minimize 
# that aswell to O(1) along with others we use HAshMap instead of HashSet in the next approach
import random

class RandomizedSet:
    def __init__(self):
        self.num_set = set()  # HashSet for fast insert/remove
        self.num_list = []    # List to maintain order for getRandom

    def insert(self, val: int) -> bool:
        if val in self.num_set:  # Check if the value already exists
            print(False)
            return False
        self.num_set.add(val)    # Add to the set
        self.num_list.append(val)  # Add to the list
        print(True)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_set:  # Check if the value exists
            print(False)
            return False
        self.num_set.remove(val)    # Remove from the set
        self.num_list.remove(val)   # Remove from the list
        print(True)
        return True

    def getRandom(self) -> int:
        if not self.num_list:  # Check if the list is empty
            print("List is empty.")
            return None
        rand_val = random.choice(self.num_list)  # Get a random element
        print("Random Choice:", rand_val)
        return rand_val

     # Get a random value


# O(1) for all functions APproach
class RandomSetOptimized:
    def __init__(self):
        self.num_dict = {}  # Dictionary to store value -> index mapping
        self.num_list = []  # List to store values for getRandom

    def insert(self, val: int) -> bool:
        if val in self.num_dict:  # Check if the value already exists
            print(False)
            return False
        self.num_dict[val] = len(self.num_list)  # Map the value to its index in the list
        self.num_list.append(val)  # Add the value to the list
        print(True)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_dict:  # Check if the value exists
            print(False)
            return False
        idx = self.num_dict[val]  # Get the index of the value in the list
        last_val = self.num_list[-1]  # Get the last value in the list

        # Swap the last value with the value to be removed
        self.num_list[idx] = last_val
        self.num_dict[last_val] = idx

        # Remove the last element from the list and the dictionary
        self.num_list.pop()
        del self.num_dict[val]
        print(True)
        return True

    def getRandom(self) -> int:
        if not self.num_list:  # Check if the list is empty
            print("List is empty.")
            return None
        rand_val = random.choice(self.num_list)  # Get a random element
        print("Random Choice:", rand_val)
        return rand_val


# Example Usage
rso = RandomSetOptimized()
rso.insert(42)
rso.insert(15)
rso.remove(42)
rso.getRandom()


        
