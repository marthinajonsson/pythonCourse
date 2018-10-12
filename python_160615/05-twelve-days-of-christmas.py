things = [
    "twelve drummers drumming,",
    "eleven pipers piping,",
    "ten lords-a-leaping,",
    "nine ladies dancing,",
    "eight maids-a-milking,",
    "seven swans-a-swimming,",
    "six geese-a-laying,",
    "five gold rings,",
    "four calling birds,",
    "three french hens,",
    "two turtle doves",
    "and a partridge in a pear tree",
]

ordinals = [
    "zeroth",   # not used, but makes things nicer
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth",
]

for day in range(1, 13):
    nth = ordinals[day]
    print("On the", nth, "day of Christmas my true love sent to me")

    if day == 1:
        print("a partridge in a pear tree")
    else:
        for t in things[-day:]:
            print(t)
    print()