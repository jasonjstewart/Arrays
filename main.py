from array_api import Array
import csv

def main():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            items = row[0].split(",",1)
            parameters=items[1].split(",")
            action = items[0]
            if action ==  'CREATE':
                print(action,parameters)
                array=Array()
            elif action == 'DEBUG':
                array.debug_print()
            elif action == 'ADD':
                print(action,parameters)
                array.add(parameters[0])
            elif action == 'SET':
                print(action,parameters)
                array.set(int(parameters[0]),parameters[1])
            elif action == 'GET':
                print(action,parameters)
                array.get(int(parameters[0]))
            elif action == 'DELETE' :
                print(action,parameters)
                array.delete(int(parameters[0]))
            elif action == 'INSERT':
                print(action,parameters)
                array.insert(int(parameters[0]),parameters[1])
            elif action == 'SWAP':
                print(action,parameters)
                array.swap(int(parameters[0]),int(parameters[1]))
            else:
                print("Blow up!")
            




