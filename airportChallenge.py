#file = open("testfile", 'r')


data = [lines.strip().split(" ") for lines in open('testfile', 'r')]

problems = []
while data:
        problem = {}
        problem['n'] = int(data[0][0])
        problem['m'] = int(data[0][1])
        problem["idle_times"] = data[1]
        problem["airport_graph"] = data[2:2 + problem['n']]
        problem["flights"] = sorted(data[2 + problem['n']:2 + problem['n'] + problem['m']], key = lambda flight: flight[2])
        
        data = data[2 + problem['n'] + problem['m']:]
        problems.append(problem)

#for lines in file:
#    data.append(lines.strip().split(" "))

print(problem)