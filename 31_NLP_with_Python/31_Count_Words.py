import re

def count_words(text):
	"""Count How many times each word occurs in text"""
	counts = dict()

	# Convert to Lowercase
	text = text.lower()

	# Split text into tokens
	words = re.split(r'[^\w]', text)

	# Aggregare Word Counts Using a Dictionary
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
	return counts


with open('Data/input.txt') as f:
	text = f.read()
	counts = count_words(text)

print(counts)
sorted_counts = sorted(counts.items(), key=lambda pair:pair[1], reverse=True)
print("10 Most Common Words:\nWord\tCount")
for word,count in sorted_counts[:10]:
	print(f"{word}\t{count}")
print("-"*30)
print("10 Most Least Words:\nWord\tCount")
for word,count in sorted_counts[-10:]:
	print(f"{word}\t{count}")