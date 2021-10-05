import json

from rich import print

# dictionary of the rooms
with open("zork1.rooms.json") as fp:
    rooms = {room["Name"]: room for room in json.load(fp)}

# game starts here
current_room = rooms["WEST-OF-HOUSE"]

while True:
    # game loop
    print("")
    print(
        "[bold magenta]"
        + "".join(current_room["Properties"]["DESC"])
        + "[/bold magenta]"
    )
    current_room_props = current_room["Properties"]
    print("".join(current_room_props.get("LDESC", "")))
    print(", ".join(current_room["Exits"].keys()))

    while True:
        # user input
        direction = input("Enter direction (see above): ").upper().strip()
        if direction in current_room["Exits"]:
            # NEXIT, UEXIT, CEXIT, BREXIT
            exit = current_room["Exits"][direction]
            exit_type = exit["TYPE"]
            if exit_type == "NEXIT":
                print(exit["MESSAGE"])
            elif exit_type in ["UEXIT", "CEXIT", "DEXIT"]:
                current_room = rooms[current_room["Exits"][direction]["TO"]]
                break
        else:
            print("You can't do that!\n")
