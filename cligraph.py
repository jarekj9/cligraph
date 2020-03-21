test_list=[100,100,5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,  
200,300,400,5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,200,300,400,  
5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,  
200,300,400,5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,200,300,400,  
5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,  
200,300,400,5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,200,300,400,  
5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100,  
5,20,50,80,60,40,30,5,10,44,77,88,99,120,76,45,23,4,100]  

def cligraph(values,height=20,width=80): 
    '''Takes a list with integer values and returns string with cli graph'''
    if width < 2 : width=2

    output_string=''
    graphX = '' #single X-line of graph  
    graph = []  #contains all graphX lines  
    min_value, max_value = min(values), max(values) 
    resized_values = []  
    x_scale = [ '_' for x in range(len(values))]    # chars, which draw bottom scale 
 
    if max(values) > height:  #resize to max height  
        for value in values:  
            resized_values.append(round((value*height)/max_value))  
    values = resized_values     
  
    while len(values) > width:  #resize data and scale below max width  
        values = values[::2]    
        x_scale = x_scale[::2] 
 
 
    x_scale[0],x_scale[1],x_scale[-1] = ' ','0', '{} (Length)'.format(str(len(values)))  #add first and last number of bottom (x) scale 
    graph.append(''.join(x_scale))   
    for y in range(1,height+1): 
        if y == 1:        graphX += str(min(values))   #add y_scale 
        else:             graphX += '|' 
 
 
        for value in values: 
            if value >= y: graphX += '*'     #draws main graph
            else:          graphX += ' '  
        graph.append(graphX)  
        graphX = '' 
    graph.append('{} (Max Value)'.format(str(max_value))) 

    for line in graph[::-1]:  #graph is upside down, so ::-1
        output_string += line+'\n'

    return output_string
  
 
 
print(cligraph(test_list))

 