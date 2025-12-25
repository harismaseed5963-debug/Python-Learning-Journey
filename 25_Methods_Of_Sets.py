Set = {1,4,5,6,8,"haris",False} # Other Types of Values are also Capable within a set.
print(Set, type(Set))
# Methods :
# 01 .add (To add values into the set)
Set.add(456)
# 02 .remove (To remove a specific value from the set)
Set.remove(456)
print(Set)
# 03 .pop (To remove a random value from the set)
Set.pop()
print(Set)
# 04 .clear (To remove all values from the set)
Set.clear()
print(Set)
# Create Variables for performing operations on sets
Set1 = {1,2,3,4,5,6,7,8,9,10}
Set2 = {10,20,30,40,50,60,70,80,90,100}
# 05 .union (To add values from another set)
print(Set1.union(Set2))
# 06 .intersection (To remove values that are not common in both sets)
print(Set1.intersection(Set2))                             