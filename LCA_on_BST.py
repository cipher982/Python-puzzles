'''
Find the lowest common ancestor (LCA) from a binary search tree (BST) 
and returns the index of said ancestor node. Trees are input as a matrix 
with 0/1 representing the location of each nodes child. Each row represents
a specific node in the tree.


'''


ef question4(tree,rootVal,n1,n2):

    lca = 0
	
    def child(which):
        indexes = [i for i,x in enumerate(tree[rootVal]) if x != 0]
        if which == 'left':
            return indexes[0]
        if which == 'right':
            return indexes[1]
			
    while lca is not None:
        if rootVal > n1 and rootVal < n2:
            lca = rootVal
            return lca
        if rootVal < n1 and rootVal < n2:
            rootVal = child('right')
        if rootVal > n1 and rootVal > n2:
            rootVal = child('left')

    answer = lca(rootVal, n1, n2)
    return answer     
	
# Bases test
tree1=  [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]
# Include values other than 1?
tree2=  [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 10000000, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 'Donald Drumpf', 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]
# Oops missing a column in one row!
tree3=  [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]


print question4(tree1,5,2,4)           
# 3
print question4(tree2,5,1,4)           
# 2
print question4(tree3,5,1,6)          
# 6
