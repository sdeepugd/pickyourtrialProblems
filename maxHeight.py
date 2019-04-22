def maxHeight(stickPositions,stickHeights):
    n=len(stickPositions)
    max_height=0
    
    def findHeight(i):
        start=stickPositions[i] 
        stop=stickPositions[i+1] 
        st_hgt=stickHeights[i] 
        sp_hgt=stickHeights[i+1] 
        diff=abs(st_hgt-sp_hgt) 
        pos_diff=abs(start-stop)-1 
        global max_height
        if(pos_diff is 0):
            return
        elif(pos_diff>diff):
            offset=(pos_diff-diff)/2
            if((pos_diff-diff)%2 is not 0):
                offset=offset+1
            curr_max=offset+max(st_hgt,sp_hgt)
            max_height=max(max_height,curr_max)
        elif(pos_diff<=diff):
            offset=diff/2
            if(diff%2 is not 0):
                offset=offset+1
            curr_max=min(st_hgt,sp_hgt)+offset
            max_height=max(max_height,curr_max)
    
    for i in range(n-1):
        findHeight(i)
    return max_height
