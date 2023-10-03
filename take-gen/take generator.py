import random

films = ["Ruby Gillman, Teenage Kraken", "The Super Mario Bros. Movie", "Doogal", "Saw X", "Fast X", "Knives Out", "Shrek", "The Bad Guys"]
apps = ["YouTube", "Twitter", "Instagram", "Discord", "Facebook", "Vimeo"]
places = ["Home Depot", "Sam's Club", "SkyZone", "Lowe's", "Five Below", "Stale Pretzels", "McDonald's", "Wendy's", "KFC", "Panda Express"]
people = ["Voomy","Lily","Jesus","JL","Leo","Octo","William","Emilia"]
options = ["is just as mid as", "almost solos", "is way better than", "is far worse than", "is peak, unlike", "is insanely overrated, much like", "is insanely underrated, unlike"]
things = []

for thing in films:
    things.append(thing)

for thing in places:
    things.append(thing)

for thing in apps:
    things.append(thing)

for thing in people:
    things.append(thing)

thing1 = random.choice(things)
thing2 = random.choice(things)

print(thing1,random.choice(options),thing2)
