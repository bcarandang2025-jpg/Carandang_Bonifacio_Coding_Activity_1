# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Convert to uppercase and lowercase
print("\nUppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

# Count how many times the letter "a" appears
count_a = sentence.lower().count("a")
print("\nNumber of times 'a' appears:", count_a)

# Check if the sentence starts with "Hello"
starts_hello = sentence.startswith("Hello")
print("\nStarts with 'Hello':", starts_hello)

# Split the sentence into words and print one per line
words = sentence.split()

print("\nWords in the sentence:")
for word in words:
    print(word)