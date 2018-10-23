''' Module that simulates(not solve) the josephus problem and
leave the last survivor. '''


class Josephus:
    ''' Class that defines how funny executions can be.
    '''

    def __init__(self, n):
        self.n = n
        self.people = [1 for i in range(n)]
        # Sword remains at the hand of the first user initially
        self.current = 0

    def next_alive(self):
        # Search from next to last element
        for i in range(self.current+1, self.n):
            if self.people[i]:
                return i
        # Search from 1st element to the given element
        for i in range(0, self.current):
            if self.people[i]:
                return i
        # Return string indicating not found if not found
        return 'n'

    def kill_next(self):
        # Find the next alive person to the current one.
        person_to_kill = self.next_alive()
        if person_to_kill != 'n':
            # Kill the next alive person.
            self.people[person_to_kill] = 0
            # Hand over the sword to next alive person.
            current = self.next_alive()
            if current != 'n':
                self.current = current
                # Print a '*' for alive person
                # and '#' for slain one
                for i in range(self.n):
                    if self.people[i]:
                        if i == self.current:
                            print("(*)", end="")
                        else:
                            print("*", end="")
                    else:
                        print("#", end="")
                print()
                # Kill the next person
                self.kill_next()

    def get_last_alive_person(self):
        self.kill_next()
        return self.current

if __name__ == '__main__':
    print("\nTerminologies:-")
    print("* -> alive")
    print("# -> dead")
    print("(*) -> current sword holder\n")
    n = int(input('Please input the number of participants:-'))
    print("\nSimulations")
    joseph = Josephus(n)
    last_alive = joseph.get_last_alive_person()
    print("\nLast prisoner alive is:-")
    print(last_alive+1)
