##################################
###########Code for dimensionality
##################################

###### 2D
def dim_2():
    nodes = []
    for j in [0, 1]:
        if j == 0:
            for i in [0, 1]:
                nodes.append([i, j])
        else:
            for i in [1, 0]:
                nodes.append([i, j])
    return nodes
        
###### 3D
def dim_3():
    nodes = []
    for k in [0, 1]:
        if k == 0:
            for j in [0, 1]:
                if j == 0:
                    for i in [0, 1]:
                        nodes.append([i, j, k])
                else:
                    for i in [1, 0]:
                        nodes.append([i, j, k])
                    
        else:
            
            for i in [0, 1]:
                if i == 0:
                    for j in [1, 0]:
                        nodes.append([i, j, k])
                else:
                    for j in [0, 1]:
                        nodes.append([i, j, k])
    return nodes    
        
###### 4D
def dim_4():
    nodes = []
    for l in [0, 1]:
        if l == 0:
            for k in [0, 1]:
                if k == 0:
                    for j in [0, 1]:
                        if j == 0:
                            for i in [0, 1]:
                                nodes.append([i, j, k, l])
                        else:
                            for i in [1, 0]:
                                nodes.append([i, j, k, l])
                    
            else:
                
                for i in [0, 1]:
                    if i == 0:
                        for j in [1, 0]:
                            nodes.append([i, j, k, l])
                    else:
                        for j in [0, 1]:
                            nodes.append([i, j, k, l])
                            
        else:
            for j in [1, 0]:
                if j == 1:
                    for k in [1, 0]:
                        if k== 1:
                            for i in [1, 0]:
                                nodes.append([i, j, k, l])
                        else:
                            for i in [0, 1]:
                                nodes.append([i, j, k, l])
                else:
                    for i in [1, 0]:
                        if i== 1:
                            for k in [0, 1]:
                                nodes.append([i, j, k, l])
                        else:
                            for k in [1, 0]:
                                nodes.append([i, j, k, l])   
    
    return nodes


###### 5D
def dim_5():
    nodes_d = dim_4()
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = dim_4()
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    nodes = [*first_set, *second_set]
    
    return nodes




###### 6D
def dim_6():
    nodes_d = dim_5()
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = dim_5()
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    nodes = [*first_set, *second_set]
    
    return nodes


###### 7D
def dim_7(self):
    nodes_d = self.nodes_6
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_6
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_7 = [*first_set, *second_set]
    
    return nodes

###### 8D
def dim_8(self):
    nodes_d = self.nodes_7
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_7
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_8 = [*first_set, *second_set]
    
    return nodes

###### 9D
def dim_9(self):
    nodes_d = self.nodes_8
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_8
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_9 = [*first_set, *second_set]
    
    return nodes


###### 10D
def dim_10(self):
    nodes_d = self.nodes_9
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_9
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_10 = [*first_set, *second_set]
    
###### 11D
def dim_11(self):
    nodes_d = self.nodes_10
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_10
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_11 = [*first_set, *second_set]
    

###### 12D
def dim_12(self):
    nodes_d = self.nodes_11
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_11
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_12 = [*first_set, *second_set]

###### 13D
def dim_13(self):
    nodes_d = self.nodes_12
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_12
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_13 = [*first_set, *second_set]
    

###### 14D
def dim_14(self):
    nodes_d = self.nodes_13
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_13
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_14 = [*first_set, *second_set]
    

###### 15D
def dim_15(self):
    nodes_d = self.nodes_14
    [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
    first_set = nodes_d
    
    nodes_d = self.nodes_14
    [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
    second_set = nodes_d
    
    self.nodes_15 = [*first_set, *second_set]
    


nodes = dim_15()
