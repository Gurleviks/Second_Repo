#1
quote = "This is a quote."

#2
word = quote[5:7]

#3
upper_quote = quote.upper()  
lower_quote = quote.lower()
title_quote = quote.title()

#4
new_quote = quote.replace("quote", "")
strip_quote = quote.strip(".")

#5
name = "Wololo"
format_quote = "Hello, {}! {}".format(name, quote)

print("Original Quote:", quote)
print("Extracted Word:", word)
print("Uppercase Quote:", upper_quote)
print("Lowercase Quote:", lower_quote)
print("Titlecase Quote:", title_quote)
print("Modified Quote:", new_quote)
print("Stripped Quote:", strip_quote)
print("Formatted Quote:", format_quote)
