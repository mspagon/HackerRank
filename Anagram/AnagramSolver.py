# Author: mspagon
# Date: 5/12/18 7:58 PM

# Problem: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def find_anagram(a, b):
    array_a = [0] * 26
    array_b = [0] * 26

    for letter in a:
        index = ord(letter) - ord('a')
        array_a[index] += 1

    for letter in b:
        index = ord(letter) - ord('a')
        array_b[index] += 1

    total = 0
    for i in range(len(array_a)):
        total += abs(array_a[i] - array_b[i])

    return total


a = "akewhtklawethkdgnlkawethyklasgntalkjtnnnhnterkjthlkdthnnertkjnla"
b = "kjertnkjerhtpertpoeitoerutoiychxzgkjnwejkgtalwetkhsdfgnpesartppweitwipethzxcngkawjetnkjewant"

print(find_anagram(a, b))
