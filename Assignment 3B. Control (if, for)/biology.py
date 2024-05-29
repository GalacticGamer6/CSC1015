
print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")

skeletal_structure = input("The skeleton is (internal/external)?\n")

if skeletal_structure == "internal":
    fertilisation_type = input("The fertilisation of eggs occurs (within the body/outside the body)?\n")
    if fertilisation_type == "within the body":
        birth_method = input("Young are produced by (waterproof eggs/live birth)?\n")
        if birth_method == "waterproof eggs":
            skin = input("The skin is covered by (scales/feathers)?\n")
            if skin == "scales":
                print("Type of animal: Reptile")
            else:
                print("Type of animal: Bird")
        else:
            print("Type of animal: Mammal")
    else:
        location = input("It lives (in water/near water)?\n")
        if location == "in water":
            print("Type of animal: Fish")
        else:
            print("Type of animal: Amphibian")
else:
    print("Type of animal: Arthropod")