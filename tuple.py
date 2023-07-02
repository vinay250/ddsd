print("tuple created in the name:my_tuple")
my_tuple=('p','e','r','m','i','t')
print("tuple indexing",my_tuple[0])
print("tuple negative indexing",my_tuple[-1])
print("tuple slicing",my_tuple[1:4])
my_tuple=(4,3,2,5,[6,5])
my_tuple[4][1]=9
print("tuple changing",my_tuple)
del my_tuple[4]
print("tuple delete",my_tuple)