def odd_and_triple(lst, num):
    for i in num:
        if (i % 2 == 1) and (i % 3 == 0):
            lst.append(i)
    return lst
def count_vowels(vowels, cnt, word):
    splited_word = [char for char in word]
    for letter in splited_word:
        if letter in vowels:
            cnt += 1
    return cnt

def main():
    cnt = 0
    result = []
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    num_data = [12, 21, 36, 48, 57, 68, 73, 84, 95]
    word = "Tennessee"
    print(odd_and_triple(result, num_data))
    print(count_vowels(vowels, cnt, word))

if __name__ == "__main__":
    main()