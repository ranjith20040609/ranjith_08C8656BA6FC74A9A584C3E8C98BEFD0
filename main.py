def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices
# Create a list of products
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]

# Search for the target product "Apple"
target_product = "Apple"
result = linear_search_product(products, target_product)

# Print the result
if len(result) > 0:
    print(f"The product '{target_product}' was found at indices: {result}")
else:
    print(f"The product '{target_product}' was not found.")