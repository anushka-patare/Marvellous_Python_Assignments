def ChkVowels(vowel):
    if vowel=="a" or vowel=="e" or vowel=="i" or vowel=="o" or vowel=="u":
        print("This is a vowel.")

    else:
        print("This is a consonant.")

def main():
    print("Enter character :")
    character=input()

    ChkVowels(character)

if __name__ == "__main__":
    main()