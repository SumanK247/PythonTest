# import mem_profile
import random
import time
#New line added for SR#1234
import pandas as pd

names = ['John','Corey','Adam','Steve','Rick','Thomas']
majors = ['Math', 'Engineering','ComSci','Arts','Business']



print('Hello...')

def people_list(num_people):
	result = []
	for i in xrange(num_people):
		person = {
		             'id': i,
		             'name': random.choice(names),
		             'major': random.choice(majors)
		}
		result.append(person)
	return result

	

def people_generator(num_people):
	for i in xrange(num_people):
		person = {
		             'id': i,
		             'name': random.choice(names),
		             'major': random.choice(majors)
		         }
		yeild(person)

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()


# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()


# print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))
print ('Took {} Seconds'.format(t2-t1))