# Author : Muhammad Syafiq Mazli
## Email : m.syfqmzli@gmail.com
### Date : November 16, 2022

# If T-Rex is angry, hungry, and bored he will eat the Triceratops.
# Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
# Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
# Otherwise if T-Rex is tired, he goes to sleep.
# Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
# Otherwise if T-Rex is angry or bored, he roars.
# Otherwise T-Rex gives a toothy smile.

angry = True
bored = True
hungry = False
tired = False

if angry and hungry and bored:
    print("T-Rex will eat the Triceratops.")
elif tired and hungry:
    print("T-Rex will eat the Iguanadon.")
elif hungry and bored:
    print("T-Rex will eat the Stegasaurus.")
elif tired:
    print("T-Rex goes to sleep.")
elif angry and bored:
    print("T-Rex will fight the Velociraptor.")
elif angry or bored:
    print("T-Rex will roars.")
else:
    print("T-Rex gives a tooth smiley :)")