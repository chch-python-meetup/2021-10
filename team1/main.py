import json
from typing import Optional, Tuple

rooms = json.load(open('zork.json'))

rooms_by_name = {r['Name']: r for r in rooms}


class Game:
  CANONICAL_DIRS = {
    'NORTH': 'NORTH',
    'N': 'NORTH',
    'SOUTH': 'SOUTH',
    'S': 'SOUTH',
    'EAST': 'EAST',
    'E': 'EAST',
    'WEST': 'WEST',
    'W': 'WEST',
    'NORTHEAST': 'NE',
    'NE': 'NE',
    'SOUTHWEST': 'SW',
    'SW': 'SW',
    'NORTHWEST': 'NW',
    'NW': 'NW',
    'SOUTHEAST': 'SE',
    'SE': 'SE',
    'UP': 'UP',
    'U': 'UP',
    'DOWN': 'DOWN',
    'D': 'DOWN'
  }

  def __init__(self):
    self.room = rooms[0]
    self.flags = {}
    
  def repl(self):
    room = rooms[0]

    print("You are standing in an open field west of a white house, with a boarded front door.")
    print("There is a small mailbox here.")

    while True:
      command = input('> ').upper()
      
      direction = self.canonical_dir(command)
      if direction is not None:
        name, msg = self.can_move(room, direction)
        if name:
          room = rooms_by_name[name]
          self.print_room_name(room)
        else:
          print(msg)
        continue

      if command in ['QUIT', 'Q', 'EXIT']:
        print("Thanks for playing zork.")
        break
      elif command == 'LOOK':
        self.print_room(room)
      elif command == 'DAMN':
        print("Such language in a high-class establishment like this!")
      else:
        print("I beg your pardon?")

      print()

  def print_room_name(self, room):
    short_description = ''.join(room['Properties']['DESC'])
    print(short_description)

  def print_room(self, room):
    self.print_room_name(room)
    if 'LDESC' in room['Properties']:
      print(''.join(room['Properties']['LDESC']))

  def canonical_dir(self, direction):
    return self.CANONICAL_DIRS.get(direction)

  def can_move(self, room, direction) -> Tuple[Optional[str], Optional[str]]:
    # Returns a tuple of next Room name and "error" message
    move = room['Exits'].get(direction)
    if move is None:
      return (None, f"You can't go {direction}")
    if move['TYPE'] == 'NEXIT':
      return (None, move['MESSAGE'])
    elif move['TYPE'] == 'UEXIT':
      return (move['TO'], None)
    elif move['TYPE'] == 'CEXIT':
      if self.flags.get(move['COND']):
        return (move['TO'], None)
      else:
        return (False, move['ELSE'])
    else:
      raise ValueError(f"unexpected move type {move['TYPE']}")



if __name__ == "__main__":
  game = Game()
  game.repl()
