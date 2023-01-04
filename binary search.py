def printer(foo):
    def inner(*args):
        print (result :=foo(*args))
        return result
    return inner

@printer
def solution(phonebook,name):
    if len(phonebook) <= 0:
        return 'Phonebook is empty!'
    first = 0
    last = len(phonebook) - 1
    while last >= first:
        middle = (last-first)//2 + first
        middle_name = phonebook[middle]['name']
        if phonebook[middle]['name'] == name:
            return phonebook[middle]['number']
        if name > phonebook[middle]['name']:
            first = middle + 1
        elif name < phonebook[middle]['name']:
            last = middle - 1
    return "Name not found!"

phonebook = [
    {"name":"Alex Bowman","number":"48-2002"},
    {"name":"Aric Almirola","number":"10-1001"},
    {"name":"Bubba Wallace","number":"23-1111"},
    {"name":"Chase Elliott","number":"9-9900"},
    {"name":"Denny Hamlin","number":"11-0022"},
    {"name":"John Logano","number":"22-2299"},
    {"name":"Kevin Harvick","number":"4-1154"},
    {"name":"Kyle Busch","number":"18-3002"},
    {"name":"Kyle Larson","number":"5-2234"},
    {"name":"Matt Dibenedetto","number":"21-1102"}
]

# # solution(phonebook, 'Alex Bowman')  # '48-2002'
# solution(phonebook, 'None')  # 'Name not found!'
# solution([], 'Alex Bowman')  # 'Phonebook is empty!'
# solution(phonebook, 'Chase Elliott')
list_ = [
    ['Denny Hamlin', '11-0022'],
    ['Chase Elliott', '9-9900'],
    ['Alex Bowman', '48-2002'],
    ['Matt Dibenedetto', '21-1102'],
    ['Kyle Larson', '5-2234'],
  ]

for q,a in list_:
    assert solution(phonebook,q) == a