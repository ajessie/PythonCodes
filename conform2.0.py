#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]

def pleaseConform(caps):
    #Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

                                                                            #Determine intervals where caps are on in the same direction
    for i in range(len(caps)):                                              #If "i" is in the range of cap array
        if caps[start] != caps[i]:                                          #If the start value doesn't equal the current value being evaluated
                                                                            
            intervals.append((start, i - 1, caps[start]))                   #Each interval is a tuple with 3 elements (start, end, type)
            
            if caps[start] == 'F':                                          #If the element being evaluated is "F"
                forward += 1                                                #Add to the forward counter
            else:
                backward += 1                                               #If not "F", then by default "B", add to backward counter
            start = i                                                       #Start evaluating at current element in array 

    
    intervals.append((start, len(caps) - 1, caps[start]))                   #Need to add the last interval after for-loop completes execution

    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
 
                                                                            #Print (intervals)
                                                                            #Print (forward, backward)
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
                                                                            #Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                print ('Person at position', t[0], 'flip your cap!')
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')
                
            
pleaseConform(caps)