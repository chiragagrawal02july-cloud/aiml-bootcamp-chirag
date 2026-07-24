with open("large_file.txt" , "w") as file :
    for i in range (1,5000001):
        file.write(f"This is line {i}\n")

print("File created successfully")

total_lines = 0
words_count = 0

Search_word = "100"
with open("large_file.txt" , "r") as file :
    for line in file :
        total_lines += 1
    if Search_word in file :
        words_count += 1
print("total lines : ", total_lines)
print(f'lines containing "{Search_word}" : ' , words_count)