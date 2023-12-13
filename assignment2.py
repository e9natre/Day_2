import random
import string
def random_name():
    first_name = ''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(8, 12))).capitalize()
    last_name = ''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(8, 12))).capitalize()
    return first_name, last_name


def random_age():
    return random.randint(18, 81)

def random_person():
	first_name, last_name = random_name()
	result = {
		"first_name": first_name,
		"last_name": last_name,
		"age": random_age()
	}

	return result
print(random_person())

def getlist(num_people):
     people_list = [{'name':f'Person{x}', 'age': random.randint(18,81)} for x in range(num_people)]
     sorted_people = sorted(people_list, key=lambda x: x['age'], reverse=True)
     for person in sorted_people:
         print(person)
         return sorted_people
