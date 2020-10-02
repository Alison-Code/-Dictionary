print("\nWELCOME TO MY DICTIONARY")

d={"seethe":"boil",
    "amicable":"friendly",
    "noel":"christmas",
    "formidable":"intimidating"
}
print("WORDS -> seethe , amicable , noel , formidable")
print("Choose your word and write here to know the meaning")
wrd = input()

if wrd not in d:
    print("THE WORD IS NOT IN THE DICTIONARY")

else:
    print("The meaning of the word is", d[wrd])
