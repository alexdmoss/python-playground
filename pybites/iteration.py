from logger import log

dict1 = dict(thor='lightning', hulk='smash')
dict2 = dict(iron_man='lasers', dr_strange='wizard')
list1 = ['luke', 'leia', 'han solo', 'chewbacca', 'r2d2', 'c3po']
list2 = ['luke', 'anakin', 'leia', 'yoda', 'kenobi']
sentence = 'Star Wars is better than Trek'

merged_dict = dict(**dict1, **dict2)
print(merged_dict)

min_len = 4
log.info(f'Match if all values are >= {min_len} in length')
print(all(len(value) >= min_len for value in list1))

substr = 'han'
log.info(f'Check if any values contain {substr}')
print(any(substr in value for value in list1))

log.info('Iterate over a sentence, including its index')
words = sentence.split()
for count, name in enumerate(words):
    print(count, name)

log.info('Iterate over a sentence, printing even indices only')
print([value for index, value in enumerate(words, start=1) if not index % 2])

set1 = set(list1)
set2 = set(list2)

log.info('Set Operations from lists: Unique in {list1} from both sets')
print(set1 - set2)

log.info('Set Operations from lists: Unique in {list2} from both sets')
print(set2 - set1)

log.info('Set Operations from lists: In both lists')
print(set2 & set1)

log.info('Set Operations from lists: In either list')
print(set2 ^ set1)
