import test

pdf_files = ["/Users/christian/OneDrive/PhD/Thesis/Publications/Muller2022JA - Confinement.pdf",
             "/Users/christian/OneDrive/PhD/Thesis/Publications/Muller2023JMPS - printSWR.pdf"]

# Load PDF text into a collection
pdf_text_collection = [test.PDF(pdf_file) for pdf_file in pdf_files]

# User input
#user_input = "We are using GFMD in this study."
user_input = "above a certain thickness, the behavior is identical to semi-infinite"

# Find the best match
match, sentence, similarity = test.find_best_match(user_input, pdf_text_collection)

# Print the best match and its similarity score
if match:
    print("Best Match:")
    print(match)
    print(sentence)
    print("Similarity Score:", similarity)
else:
    print("No matching content found.")
