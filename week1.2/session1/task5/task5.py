# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Brazil"] = "Amazon"
rivers["Egypt"] = "Nile"
print(rivers)

# Display all the keys
print(rivers.keys())
# Display all the values

# Display all the key:value pairs, as tuples
print(rivers.values())

# Delete an entry from the rivers database
rivers.pop("Leeds")
print(rivers)
