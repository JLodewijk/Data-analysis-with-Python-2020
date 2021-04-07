#!/usr/bin/env python3

def n_unique_chars(word):
   
    G=[]
    for i in word:
        if i not in G:
            G.append(i)
    return len(G)

def distinct_characters(L):
    dist_dict = {}
    for word in L:
        dist_dict[word] = n_unique_chars(word)

    return dist_dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
