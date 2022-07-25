name = "john"
print(f"Hey, {name} would you like to learn some Python today?")

name_lowercase = "JOHN"
print(name_lowercase.lower())
print(name_lowercase.upper())
print(name_lowercase.title())

author = "albert einstein"
quote = " \tA person who never made a mistake\n never tried anything new. "

print("{} once said, {}".format(author.title(), quote.strip()))