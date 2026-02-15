import random

people = ["Liam", "Olivia", "Noah", "Ava",
          "James", "Amelia", "William", "Emma"]

skills = ["coding", "art", "testing", "management", "marketing"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Globals
# Choosing a random element from a set
# Moudlar counting

def two_skills_to_each_person(people, skills):
    umiejetnosci = dict()
    
    for name in people:
        two_skills = set()
        while len(two_skills) < 2:
            two_skills.add(random.choice(skills))
        umiejetnosci.update({name: two_skills})
    return umiejetnosci

def print_days_4_times(days):
    for i in range(len(days)*4):
        print(days[i%len(days)], end=", ")


def main():
    umiejetnosci = two_skills_to_each_person(people, skills)
    print(umiejetnosci)

    print()

    print_days_4_times(days)

    

main()