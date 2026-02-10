import pickle

with open("laptop_cleaned.pkl", "rb") as f:
    obj = pickle.load(f)

print(type(obj))
print(obj)
