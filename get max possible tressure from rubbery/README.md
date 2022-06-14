# what's in the .py

I solved the problem and wrote it inside a script called waje.py file attached in the submission. The python script contains two part: the main function that returns the value given the array of houses and the test part to test the function against test cases

## Methodology:

I solved this problem by starting at point zero in the array and evaluating and keeping track of maximum possible treasures raided from previous houses to be used to evaluate on the next house as it stands as representation for houses passed/raided, hence this problem is a typical example of Dynamic Programming. 
I have labels (“max_raid_0”,”max_raid_1”) holding the maximum amount raided while not raiding consecutive houses to breach the security alarm. I called the function trasv_to_max_bag. i.e transverse-to-accumulate-for-maximum-bag

## Results and evaluation:

I ran the scripts with a few test cases and the result was a match for all.
The time complexity is O(n*k) = O(n): it ran the n length array executing few k commands
The Auxiliary Space is O(k): no array was stored temporarily in memory at run time
The Space Complexity is O(n*k) = O(n): an array is needed in the input with few k variable temporary space used as well

#### Thanks and regards.

#### © Akinyemi sodiq


