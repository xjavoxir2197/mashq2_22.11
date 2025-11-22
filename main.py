import random
import string

task11 = random.randint(1, 6)
print(task11)

task12 = random.randint(1000, 9999)
print(task12)

sample_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
task13 = random.sample(sample_list, 2)
print(task13)

task14 = random.randint(0, 100)
if task14 % 2 == 0:
    print("juft")
else:
    print("toq")

task15 = ''.join(random.choices(string.ascii_lowercase, k=10))
print(task15)

task16 = random.randint(1, 100)
if task16 > 50:
    print("katta")
else:
    print(task16)

task17 = random.choice(["heads", "tails"])
print(task17)

task18 = random.randint(1, 20)
if task18 % 3 == 0:
    print("3 ga bo'linadi")
else:
    print("3 ga bo'linmaydi")

sample_list2 = ['red', 'green', 'blue', 'yellow']
chosen = random.choice(sample_list2)
sample_list2.remove(chosen)
print(chosen)
print(sample_list2)

task20 = random.randint(1, 1000)
print(task20 * task20)
