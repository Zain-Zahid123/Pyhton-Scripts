# Creating a list of cloud service providers
list_of_cloud = ["AWS", "Azure", "GCP", "Digital Ocean"]
print(list_of_cloud)  # Printing the initial list

# Adding a new cloud provider "Oracle" at the end of the list
list_of_cloud.append("Oracle")
print(list_of_cloud)  # Printing the updated list

# Inserting "Salesforce" at index 2 (3rd position)
list_of_cloud.insert(2, "Salesforce")
print(list_of_cloud)  # Printing the list after insertion

# Printing the length (total number of elements) of the list
print(len(list_of_cloud))

# Iterating through the list and printing each cloud provider
for cloud in list_of_cloud:
    print(cloud)

# Printing numbers from 1 to 10 using range()
for i in range(1, 11):
    print(i)  # Prints numbers from 1 to 10