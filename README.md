# pickyourtrialProblems

Palindrome Counter:
The program generates indices with the following rule:

                (0,1)
                /   \
    (0+1,0) (0,0+1) (0+1,1) (0,1+1)
    
    We recurse with the following cases
    case 1:start index is greater than stop index
    case 2:start index is less than length of string
    case 3:stop index is less than length of string
    if the above cases are not met then the indixes are added to a set to avoid duplication and recursion is called twice . One with incrementing the start index and other with incrementing the stop index.
    
    Once the recursion completes then the substring are generated with the indices stoed in the set and checked for palindrome.If it is a palindrome the counter is incremented.
    
 
    
Mud Walls:
The max height of the mud walls can be found by applying a formulae:
let us assume the difference between the two sticks as pos_diff
and the difference of the height as diff
then the formulae is 
if the pos_diff > diff
then find the median from the difference of (pos_diff and diff) and add it to the max of the two stick heights
if the pos_diff <= diff
then find the median of diff alone and add it to the min of the stick heights.
