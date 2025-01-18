def minion_game(string:str):
    VOWELS = ['A','E','I','O','U']
    n=len(string)
    k_score, s_score = 0,0
    
    for i in range(n):
        if string[i] in VOWELS:
            k_score += (n-i)
        else:
            s_score += (n-i)

    if k_score > s_score:
        print(f"Kevin {k_score}")
    elif k_score < s_score:
        print(f"Stuart {s_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
