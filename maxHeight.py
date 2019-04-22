def maxHeight(stickPositions,stickHeights):
    # stickPositions=[1,3,7]
    # stickHeights=[4,3,3]
    n=len(stickPositions)
    max_height=0
    
    def findHeight(i):
        start=stickPositions[i] #3
        stop=stickPositions[i+1] #7
        st_hgt=stickHeights[i] #3
        sp_hgt=stickPositions[i+1] #3
        diff=abs(st_hgt-sp_hgt) #0
        pos_diff=abs(start-stop)-1 #4
        global max_height
        if(pos_diff is 0):
            return
        elif(pos_diff>diff):
            offset=(pos_diff-diff)/2
            curr_max=offset+max(st_hgt,sp_hgt)
            max_height=max(max_height,curr_max)
        elif(pos_diff<diff):
            median=diff/2
            if(diff%2 is not 0):
                median=median+1
            curr_max=min(st_hgt,sp_hgt)+median
            max_height=max(max_height,curr_max)
    
    for i in range(n-1):
        findHeight(i)
    return max_height
