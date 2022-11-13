import sys


def main():
    file2 = open("resultater/finishedSanitized.txt", "r", encoding="utf8")

    letters = "akbarcloghill"

    let_set = set(letters)

    for i, song in enumerate(file2):
        if all(x.lower() in let_set for x in set(song.strip())):
            if len(letters) == len(song.strip()):
                print(song.strip())


if __name__ == "__main__":
    main()
