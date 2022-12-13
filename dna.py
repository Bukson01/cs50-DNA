import csv
import sys

#shortening the argument vector
args = sys.argv

#Storge for the STR values
STRS_H = []


def main():

    # TODO: Check for command-line usage
    if len(args) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    database = load_database()

    # TODO: Read DNA sequence file into a variable
    sequence = load_sequence_data()

    # TODO: Find longest match of each STR in DNA sequence
    target = str_sequence_counter(sequence)

    # TODO: Check database for matching profiles
    result = search_database(target, database)

    print(result)


def load_database():
    database = []

    with open(args[1], "r") as f:
        reader = csv.DictReader(f)

        # Update STR sequences header, the first
        # [0] is name, so we drop it out.
        global STRS_H
        STRS_H = reader.fieldnames[1:]

        for row in reader:
            for i in STRS_H:
                row[i] = int(row[i])
            database.append(row)

    return database


def load_sequence_data():
    with open(args[2], "r") as f:
        sequence = f.read()

    return sequence


def str_sequence_counter(sequence):
    # Initialize counter all values to zero.
    counter = {i: 0 for i in STRS_H}

    for j in counter:
        n = find_maxnum_key(j, sequence)
        counter[j] = n

    return counter


def find_maxnum_key(key, text):
    count = 0
    pattern = key
    while pattern in text:
        count += 1
        pattern += key

    return count


def search_database(target, database):
    for people in database:
        if all([people[k] == target[k] for k in STRS_H]):
            return people["name"]

    return "No match"

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
