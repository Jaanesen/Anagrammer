import sys


def main():
    songs = open('resultater/spotify-uttrekk.txt', 'r', encoding="utf_8")
    sanitizedSongs = open("temp/sanitized3.txt", "a", encoding="utf_8")

    for n in songs:
        alpha = n
        if "(" in n:
            alpha = n.replace(" ", "").split("(")[0]
        if "-" in n:
            alpha = n.replace(" ", "").split("-")[0]
        alpha = ''.join(filter(str.isalpha, alpha))
        if alpha.strip() != "":
            sanitizedSongs.write(alpha.lower() + "\n")

    songs.close()
    sanitizedSongs.close()

    lines_seen = set()  # holds lines already seen

    outfile = open("resultater/finishedSanitized.txt", "w", encoding="utf_8")
    for line in open("temp/sanitized3.txt", "r", encoding="utf_8"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()


if __name__ == "__main__":
    main()
