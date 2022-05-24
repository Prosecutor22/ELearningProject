index = 1
with open('logs.txt') as infile:
   for line in infile:      
        line = line.replace('\n', '').replace('\x00', '')
        if(line in ['[]', '', ' '] or (not line.startswith('['))):
            continue
        with open('log{}.json'.format(index), 'w') as outfile:
            outfile.write(line)
            index += 1
