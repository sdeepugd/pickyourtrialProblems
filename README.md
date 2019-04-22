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
    
 
    
