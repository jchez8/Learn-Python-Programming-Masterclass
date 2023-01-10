data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for plant in data:
    if "Flower" in plant:
        flowers.append(plant)
    else:
        shrubs.append(plant)
print(flowers)
print()
print(shrubs)
# if "Shrub" in data:
    # print(data)

# range(len(data)):
    # print(i)
    
    # if Flower in data:
    #     flower = data[i]
    #     flowers.append(flower)
    # else:
    #     shrub = data[i]
    #     shrubs.append(shrub)

# Need to determine if value in list is includes flower or shrub 