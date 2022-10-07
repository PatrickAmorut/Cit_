
def write_quiz(text):
    
    with open("test.txt", "w") as f:
        f.write(text)

def read_quiz():
    with open("test.txt") as f: # file found in working directory other wise specify directory
        # for ans in range(len("test.txt")):
            print(f.read())


write_quiz("1.A, 2.B, 3.C, 4.D")
read_quiz()
