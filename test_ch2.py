
# Write a function that takes a string and return the shortest and longest words within it.
# String 'A cow jumped over the moon'


def test_shortest_word():
    text = ('Today they went to have some coffee').split()
    short = text[0]

    for words in text:
        if len(short) > len(words):
            short = words

    print(short)


# text = input("ENTER TEXT: ").split()
# short = text[0]
#
# for words in text:
#     if len(short) > len(words):
#         short = words
#
# print(short)










