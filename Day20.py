file = open('dog_breeds.txt')

#reader = open('dog_breeds.txt')

#reader.close

#open('abc.txt')

#open('abc.txt', 'r')

#open('abc.txt', 'w')

#type(file)

#file = open('dog_breeds.txt', 'rb', buffering=0)
#type(file)

with open('dog_breeds.txt', 'r') as reader:
    print(reader.read())