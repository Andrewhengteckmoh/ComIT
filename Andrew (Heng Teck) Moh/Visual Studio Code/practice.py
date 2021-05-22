#%%
print("Hello world")

#%% --define function
def yesman():
    print("I'm the best!")

yesman()   

# %% iteration
Digimon = ["Pikachu", "Ratata", "Mewtwo"]
for x in Digimon:
    print (x)

# %% need to fix input prompt x,y,z values
x = input()
y = input()
z = input()

if x == y == z:
    print("Equilateral triangle")

elif x == y or y == z or z == x:
    print("Isosceles triangle")

else:
    print("Scalene triangle")



# %% upper case & stringing strings.
a = "Hello, World!"
print(a.upper())

b = "Hello"
c = "World"
d = b + " " + c
print (d)


