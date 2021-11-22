# Given a sorted array, return the index of a given value, or -1 if the element cannot be found.
arr = [ 1, 2, 5, 9, 10, 12, 15, 21, 26 ]
find = [ 3, 5, 7, 12 ]
for index1 in range ( 0 , len( find ) ) :
    flag = 0
    for index2 in range ( 0 , len( arr ) ) :
        if find [ index1 ] == arr [ index2 ] :
            print ( find [ index1 ] , "found at index" , index1 )
            flag = 1
            break
    if flag == 0 : print ( find [ index1 ] , "not found" )