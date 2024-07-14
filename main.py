#!/usr/bin/env python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
    with open("./books/frankenstein.txt") as f:
        book = f.read()
    letters = {}
    for i in alphabet:
        letters[i] = letterCount(book,i)
    numWords = wordCount(book)
    print(f"-----Stats for the book fed into the program-----\n\nThere are {numWords} words in this book.\n")
    print(f"Here's an analysis of the letters in this book:\n")
    for i in alphabet:
        print(f"The letter \'{i}\' was found {letters[i]} times.")
    print("\n-----               End Stats               -----")

def wordCount(text):
    words = text.split()
    count = 0
    for i in words:
        count += 1
    return count

def letterCount(text, letter):
    text = text.lower()
    count = 0
    for i in text:
        if i == letter:
            count += 1
    return count
main()
