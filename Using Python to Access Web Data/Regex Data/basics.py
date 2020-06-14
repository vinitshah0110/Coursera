import re

#Capturing Groups
result = re.search(r'^(\w*), (\w*)$', 'Shah, Vinit')
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])

print('{} {}'.format(result[2], result[1]))

def rearrange_name(name):
    result = re.search(r'^(\w*), (\w*) (.*)$', name)
    if result is None:
        return name
    return '{} {} {}'.format(result[2],result[3], result[1])

name = rearrange_name('Shah, Vinit N.')
print(name)

def rearrange_name1(name):
    result = re.search(r'^([\w .-]*), ([\w .-]*)$', name)
    if result is None:
        return name
    return '{} {}'.format(result[2],result[1])

name = rearrange_name1('Sharma, Ritika R.')
print(name)


#{} Repetition Qualifiers
print(re.search(r'[a-zA-z]{5}', 'Vinit Sha'))
print(re.findall(r'[a-zA-z]{5,10}', 'Vinit Ritika'))


#Extracting a PID
log = 'A string that also has numbers [12345]'
result = re.search(r'\[(\d+)\]', log)
print(result[1])

log = 'A string 01 that also 2 has numbers 12345'
result = re.findall(r'([0-9]+)', log)
num_list = list()
for item in result:
    num_list.append(int(item))
print(sum(num_list))

def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], (result[2]))

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None


#Splitting and Replacing
print(re.split(r'[.?!]', 'One sentence. Another one? third one!'))
print(re.split(r'([.?!])', 'One sentence. Another one? third one!'))
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))
print(re.split(r"\bthe|\ba", "One sentence. Another one? And the last one!"))

print(re.sub(r'[\w.]+@[\w.]+', '[EMAIL]','Received an email for admin@my.example.com'))

print(re.sub(r'([\w]*), ([\w]*)',r'\2 \1','Shah, Vinit'))
