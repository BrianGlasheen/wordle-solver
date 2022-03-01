words = []

with open("wordbank.txt", "r") as f:
    words = list(map(lambda x : x.strip(), f.readlines())) 

for i in range(6):
    guess = input("enter the word you guessed\n>>> ")
    result = input("enter the wordle info using one capital\nletter for the color of the guess(YYBGB)\n>>> ")

    for i, (color, letter) in enumerate(zip(result, guess)):
        if color == "Y":
            words = [x for x in words if x[i] != letter and letter in x]
        
        if color == "B":
            words = [x for x in words if not letter in x]

        if color == "G":
            words = [x for x in words if x[i] == letter]

    print(f"please guess {words[0]}")