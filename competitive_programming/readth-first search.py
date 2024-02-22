from collections import deque

grath = {}
grath ['you'] = ['bob', 'claire', 'alice']
grath['bob']= ['anuj', 'peggy']
grath['alice']= 'peggy'
grath['peggy']= []
grath['claire']= ['tom', ' jonny']
grath['anuj']= [] 
grath['tom']= []
grath['jonny'] =  []


def is_seller(name):
    return len(name)%3 == 0

def search(name):
    search_queue = deque()
    search_queue+= grath[name]
    searched =[]
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print(f'{person} is seller!')
                return True
            else:
                searched.append(person)
                search_queue+= grath[person]
    return False 

search('you')           

