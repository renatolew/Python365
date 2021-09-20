# Write a Python program to create a list of random integers and randomly select multiple items from the said list.

import random
print("Create a list of random integers:")
population = range(0, 100)
sample_list = random.sample(population, 10)
print(sample_list)
rndm_elements = 4
print("\nRandomly select {} multiple items from the said list:".format(rndm_elements))
rndm_result = random.sample(sample_list, rndm_elements)
print(rndm_result)
rndm_elements = 8
print("\nRandomly select {} multiple items from the said list:".format(rndm_elements))
rndm_result = random.sample(sample_list, rndm_elements)
print(rndm_result)