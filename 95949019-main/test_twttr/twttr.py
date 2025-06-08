

def main():
    word = input("input: ").strip()
    answer = shorten(word)
    print(f"Output: {answer}")




def shorten(word):
    answer = ""
    for letter in word:
        if letter in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            letter = ""
        answer += letter
    return answer




if __name__ == "__main__":
    main()





# user_input = input("Input: ").strip()
# answer = ""
# for letter in user_input:
#     if letter in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
#         letter = ""
#     answer += letter
# print(f"Output: {answer}")
