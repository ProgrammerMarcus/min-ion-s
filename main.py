import experiment
import extract
import source

# print(experiment.experiment(source.get_sources()))

opinion1 = """A warm-hearted waiter
greets us. The restaurant has
excellent Mexican cuisine,
but the slow service...""".replace("\n", " ")
opinion2 = """We went there last night. No allergic reactions. The
shrimp tacos and house fries are my standbys. The fries
are sometimes good and sometimes great, and the spicy
dipping sauce they come with is to die for. Full beer
menu and long cocktail lists, all reasonable prices.""".replace("\n", " ")
extract.extract(opinion2)

# extract.extract(source.get_sources()[1])
