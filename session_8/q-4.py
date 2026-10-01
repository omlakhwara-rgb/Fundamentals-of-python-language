#4.Given a Flipkart product description string, write a Python script that extracts and prints the first word, last word, and the total number of words using string methods split(), indexing, and len().

des = "Hello my name is Om Lakhawara"

words = des.split()

print("First word:", words[0])
print("Last word:", words[-1])
print("Total words:", len(words))