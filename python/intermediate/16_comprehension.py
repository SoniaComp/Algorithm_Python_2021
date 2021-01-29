'''
list comprehensions
dictionary comprehensions
set comprehensions
generator comprehensions
'''
input_list = []
variable = [out_exp for out_exp in input_list if out_exp == 2]

# This can be really useful to make lists quickly. It is even preferred by some instead of the filter function. List comprehensions really shine when you want to supply a list to a method or function to make a new list by appending to it in each iteration of the for loop. 

some_dict={}
{v: k for k, v in some_dict.items()}

# set
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}

# generator - more memory efficient
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
  print(x)
  # Outputs numbers
  