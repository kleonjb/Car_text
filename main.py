import ast

file_name = "cap5.txt"

def save_value(input_value, filename):
    with open(filename, 'w') as f:
        f.write(input_value)


def load_value(filename):
    with open(filename, 'r') as f:
        read = f.read()
    return read

def sorting(filename):
    file = open('cap5.txt')
    lines = sorted(file.readlines())
    file.close()

def delete(filename):
    import os
    os.remove('cap5.txt')


try:
    values = ast.literal_eval(load_value(file_name))
    print('loaded values:', values)
except:
    print('creating a new file...')
    values = {}
x=0
str(x)
quit = 'go'
while True:
    model = 'model'
    title = 'title'
    features = 'features'
    rating = 'rating'
    values[model, x] =  input('what is the model of the car? ')
    save_value(str(values), file_name)
    values[title, x] = input('what is the title of the car? ')
    save_value(str(values), file_name)
    values[features, x] = input("what features does the care have? ")
    save_value(str(values), file_name)
    values[rating, x] = input('what is the cars current rating? ')
    save_value(str(values), file_name)
    print(values['model', x], values['title', x], values['features', x], values['rating', x])
    x=x+1
    quit = input('press "Q" to quit or anything to continue ')
    if quit == 'delete':
        delete(file_name)
        import sys
        sys.exit(0)
    if quit == 'Q':
        import sys
        sys.exit(0)
