# Function to extract keywords from a list
def extract_keywords(lst):
    keywords = {'apple', 'banana', 'orange', 'grape', 'mango'}
    extracted_keywords = [word for word in lst if word.lower() in keywords]
    return extracted_keywords


# Declare a list
my_list = ['Apple', 'Banana', 'Cherry', 'Orange', 'Grape', 'Kiwi', 'Mango']
print("Original List:",my_list)
# Extract keywords from the list
extracted_keywords = extract_keywords(my_list)

# Print the extracted keywords
print("Extracted keywords:", extracted_keywords)
