def badge_maker(name):
    return "Hello, my name is " + name + "."


def batch_badge_creator(names):
    return ["Hello, my name is " + name + "." for name in names]

def assign_rooms(speakers):
    room_assignments = []
    for i, speaker in enumerate(speakers, start=1):
        room_assignments.append("Hello, " + speaker + "! You'll be assigned to room " + str(i) + "!")
    return room_assignments


def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)
    
    for badge in badges:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)

