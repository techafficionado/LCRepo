# LCRepo

# Compare 2 lists:
1) Sort and ==
test_list1.sort() 
test_list2.sort() 
  
if test_list1 == test_list2: 
    print ("The lists are identical") 
    
2) Counter
if collections.Counter(test_list1) == collections.Counter(test_list2): 
    print ("The lists are identical") 
