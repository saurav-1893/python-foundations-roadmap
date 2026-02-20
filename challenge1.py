f = open("C:\\Users\\saura\\Documents\\chatgpt-roadmap\\Resources\\challenge1.txt")

line_count = 0
word_count = 0
for line in f:
    words = line.split()
    line_count += 1
    word_count += len(words)

print('Number of lines:', line_count)
print('Number of words:', word_count)
f.close()

