# Just testing the package we've installed
import gibberish

number_to_generate = int(input("How many random words would you like? "))
gib = gibberish.Gibberish()

print(gib.generate_words(number_to_generate))
