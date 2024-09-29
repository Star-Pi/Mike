meme_dict = {
            "CRINGE": "Something awkward or embarrassing",
            "LOL": "A response to something funny",
            "ROFL": "response to a joke",
            "SHEESH": "disapprove"
            }

word = input("Write a word you do not understand, (write it in all capital letters.): ")

if word in meme_dict.keys():
        print(meme_dict[word])
        print("NT")
else:
    print("Sorry, The Word You Put In Is Not In The Dictionary Of Memes")
