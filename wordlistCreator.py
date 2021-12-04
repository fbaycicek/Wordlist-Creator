import wordlist

min = int(input("Minimum Value: "))
max = int(input("Maximum Value: "))

content = input("Characters to be Found in The Wordlist: ")

file_name = input("File Name: ")


create = wordlist.Generator(content)

try:
    with open(file_name,"a") as file:
        total_word = 0
        for i in create.generate(min,max):
            file.write(i)
            file.write("\n")
            total_word += 1
        print("Total Word Count = "+str(total_word))

except ValueError:
    print("Please Enter Correct Values!")