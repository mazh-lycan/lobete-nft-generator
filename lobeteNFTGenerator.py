from PIL import Image 
from IPython.display import display 
import random
import json

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

bg = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
bg_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

cuerpo = ["0", "1", "2", "3", "4", "5", "6"] 
cuerpo_weights = [20, 20, 20, 20, 5, 5, 10]

pelaje = ["0", "1", "2", "3"] 
pelaje_weights = [30, 30, 25, 15]

cola = ["7", "9", "E"] 
cola_weights = [30, 40, 30]

boca = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"] 
boca_weights = [10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 2.5, 5, 2.5, 2.5, 2.5]

nariz = ["0", "1", "2", "3", "4", "5", "6"] 
nariz_weights = [15, 15, 15, 15, 15, 15, 10]

ojos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "C", "D", "E", "F"]  # B y G exclusive!!!
ojos_weights = [10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

pelo = ["8", "D"] 
pelo_weights = [75, 25]

#DEPENDANT ON BODY COLOR
oreja = ["0", "1", "2", "3", "4", "5", "6"] #en adelante exclusive!! 
oreja_weights = [20, 20, 20, 20, 5, 5, 10]

collar = ["9"] 
collar_weights = [100]

#TODO
ropa = ["1"] 
ropa_weights = [100]

#DEPENDANT ON BODY COLOR
manos = ["0", "1", "2", "3", "4", "5", "6"]
manos_weights = [20, 20, 20, 20, 5, 5, 10]

#TODO
pulseras = ["1"] 
pulseras_weights = [100]

#TODO
botas = ["1"] 
botas_weights = [100]


# Dictionary variable for each trait. 
# Eech trait corresponds to its file name

bg_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

cuerpo_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6"
}

pelaje_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6"
}

cola_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

boca_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

nariz_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

ojos_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

pelo_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

oreja_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D"
}

collar_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

ropa_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

manos_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

pulseras_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

botas_files = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}



## Generate Traits

TOTAL_IMAGES = 100 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["BG"] = random.choices(bg, bg_weights)[0]
    new_image ["Cuerpo"] = random.choices(cuerpo, cuerpo_weights)[0]
    new_image ["Pelaje"] = random.choices(pelaje, pelaje_weights)[0]
    new_image ["Cola"] = random.choices(cola, cola_weights)[0]
    new_image ["Boca"] = random.choices(boca, boca_weights)[0]
    new_image ["Nariz"] = random.choices(nariz, nariz_weights)[0]
    new_image ["Ojos"] = random.choices(ojos, ojos_weights)[0]
    new_image ["Pelo"] = random.choices(pelo, pelo_weights)[0]
    # oreja not random, equal cuerpo color
    new_image ["Oreja"] = new_image ["Cuerpo"]
    new_image ["Collar"] = random.choices(collar, collar_weights)[0]
    new_image ["Ropa"] = random.choices(ropa, ropa_weights)[0]
    # manos not random, equal cuerpo color
    new_image ["Manos"] = new_image ["Cuerpo"]
    new_image ["Pulseras"] = random.choices(pulseras, pulseras_weights)[0]
    new_image ["Botas"] = random.choices(botas, botas_weights)[0]
    
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))


# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)


# Get Trait Counts

bg_count = {}
for item in bg:
    bg_count[item] = 0

cuerpo_count = {}
for item in cuerpo:
    cuerpo_count[item] = 0
    
pelaje_count = {}
for item in pelaje:
    pelaje_count[item] = 0

cola_count = {}
for item in cola:
    cola_count[item] = 0
    
boca_count = {}
for item in boca:
    boca_count[item] = 0
    
nariz_count = {}
for item in nariz:
    nariz_count[item] = 0
    
ojos_count = {}
for item in ojos:
    ojos_count[item] = 0
    
pelo_count = {}
for item in pelo:
    pelo_count[item] = 0
    
oreja_count = {}
for item in oreja:
    oreja_count[item] = 0

collar_count = {}
for item in collar:
    collar_count[item] = 0
    
ropa_count = {}
for item in ropa:
    ropa_count[item] = 0
    
manos_count = {}
for item in manos:
    manos_count[item] = 0
    
pulseras_count = {}
for item in pulseras:
    pulseras_count[item] = 0
    
botas_count = {}
for item in botas:
    botas_count[item] = 0
    
    
for image in all_images:
    bg_count[image["BG"]] += 1
    cuerpo_count[image["Cuerpo"]] += 1
    pelaje_count[image["Pelaje"]] += 1
    cola_count[image["Cola"]] += 1
    boca_count[image["Boca"]] += 1
    nariz_count[image["Nariz"]] += 1
    ojos_count[image["Ojos"]] += 1
    pelo_count[image["Pelo"]] += 1
    oreja_count[image["Oreja"]] += 1
    collar_count[image["Collar"]] += 1
    ropa_count[image["Ropa"]] += 1
    manos_count[image["Manos"]] += 1
    pulseras_count[image["Pulseras"]] += 1
    botas_count[image["Botas"]] += 1
    
print(cuerpo_count)
print(pelaje_count)
print(cola_count)


#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#### Generate Images    
for item in all_images:
    imback = Image.open(f'./lobetesIMG/0-back/{cuerpo_files[item["Cuerpo"]]}.png').convert('RGBA')
    im0 = Image.open(f'./lobetesIMG/0-Cuerpo/{cuerpo_files[item["Cuerpo"]]}.png').convert('RGBA')
    im1 = Image.open(f'./lobetesIMG/1-Pelaje/{pelaje_files[item["Pelaje"]]}.png').convert('RGBA')
    im2 = Image.open(f'./lobetesIMG/2-Cola/{cola_files[item["Cola"]]}.png').convert('RGBA')
    im3 = Image.open(f'./lobetesIMG/3-Boca/{cola_files[item["Boca"]]}.png').convert('RGBA')
    im4 = Image.open(f'./lobetesIMG/4-Nariz/{cola_files[item["Nariz"]]}.png').convert('RGBA')
    im5 = Image.open(f'./lobetesIMG/5-Ojos/{cola_files[item["Ojos"]]}.png').convert('RGBA')
    im6 = Image.open(f'./lobetesIMG/6-Pelo/{cola_files[item["Pelo"]]}.png').convert('RGBA')
    im7 = Image.open(f'./lobetesIMG/7-Oreja/{cola_files[item["Oreja"]]}.png').convert('RGBA')
    im8 = Image.open(f'./lobetesIMG/9-Ropa/{cola_files[item["Ropa"]]}.png').convert('RGBA')
    im9 = Image.open(f'./lobetesIMG/8-Collar/{cola_files[item["Collar"]]}.png').convert('RGBA')
    imA = Image.open(f'./lobetesIMG/A-Manos/{cola_files[item["Manos"]]}.png').convert('RGBA')
    imB = Image.open(f'./lobetesIMG/B-Pulseras/{cola_files[item["Pulseras"]]}.png').convert('RGBA')
    imC = Image.open(f'./lobetesIMG/C-Botas/{cola_files[item["Botas"]]}.png').convert('RGBA')
    
    
    #Create each composite
    comb = Image.alpha_composite(imback, im0)
    com1 = Image.alpha_composite(comb, im1)
    com2 = Image.alpha_composite(com1, im2)
    com3 = Image.alpha_composite(com2, im3)
    com4 = Image.alpha_composite(com3, im4)
    com5 = Image.alpha_composite(com4, im5)
    com6 = Image.alpha_composite(com5, im6)
    com7 = Image.alpha_composite(com6, im7)
    com8 = Image.alpha_composite(com7, im8)
    com9 = Image.alpha_composite(com8, im9)
    comA = Image.alpha_composite(com9, imA)
    comB = Image.alpha_composite(comA, imB)
    comC = Image.alpha_composite(comB, imC)
    

    #Convert to RGB
    rgb_im = comC.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./lobetesIMG/Z-FINAL/" + file_name)


#### Generate Images    
for item in all_images:
    imback = Image.open(f'./lobetesIMG/0-back/{cuerpo_files[item["Cuerpo"]]}.png').convert('RGBA')
    im0 = Image.open(f'./lobetesIMG/0-Cuerpo/{cuerpo_files[item["Cuerpo"]]}.png').convert('RGBA')
    im1 = Image.open(f'./lobetesIMG/1-Pelaje/{pelaje_files[item["Pelaje"]]}.png').convert('RGBA')
    im2 = Image.open(f'./lobetesIMG/2-Cola/{cola_files[item["Cola"]]}.png').convert('RGBA')
    im3 = Image.open(f'./lobetesIMG/3-Boca/{cola_files[item["Boca"]]}.png').convert('RGBA')
    im4 = Image.open(f'./lobetesIMG/4-Nariz/{cola_files[item["Nariz"]]}.png').convert('RGBA')
    im5 = Image.open(f'./lobetesIMG/5-Ojos/{cola_files[item["Ojos"]]}.png').convert('RGBA')
    im6 = Image.open(f'./lobetesIMG/6-Pelo/{cola_files[item["Pelo"]]}.png').convert('RGBA')
    im7 = Image.open(f'./lobetesIMG/7-Oreja/{cola_files[item["Oreja"]]}.png').convert('RGBA')
    im8 = Image.open(f'./lobetesIMG/9-Ropa/{cola_files[item["Ropa"]]}.png').convert('RGBA')
    im9 = Image.open(f'./lobetesIMG/8-Collar/{cola_files[item["Collar"]]}.png').convert('RGBA')
    imA = Image.open(f'./lobetesIMG/A-Manos/{cola_files[item["Manos"]]}.png').convert('RGBA')
    imB = Image.open(f'./lobetesIMG/B-Pulseras/{cola_files[item["Pulseras"]]}.png').convert('RGBA')
    imC = Image.open(f'./lobetesIMG/C-Botas/{cola_files[item["Botas"]]}.png').convert('RGBA')
    
    
    #Create each composite
    comb = Image.alpha_composite(imback, im0)
    com1 = Image.alpha_composite(comb, im1)
    com2 = Image.alpha_composite(com1, im2)
    com3 = Image.alpha_composite(com2, im3)
    com4 = Image.alpha_composite(com3, im4)
    com5 = Image.alpha_composite(com4, im5)
    com6 = Image.alpha_composite(com5, im6)
    com7 = Image.alpha_composite(com6, im7)
    com8 = Image.alpha_composite(com7, im8)
    com9 = Image.alpha_composite(com8, im9)
    comA = Image.alpha_composite(com9, imA)
    comB = Image.alpha_composite(comA, imB)
    comC = Image.alpha_composite(comB, imC)
    

    #Convert to RGB
    rgb_im = comC.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./lobetesIMG/Z-FINAL/" + file_name)