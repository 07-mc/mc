import matplotlib.pyplot,json
file = open("score.json")
l = [0]
for n in json.load(file):
    l.append(n)
file.close()
matplotlib.pyplot.plot(range(len(l)),l)
matplotlib.pyplot.show()
