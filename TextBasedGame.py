# Ronald Justyn Ward

# main function that has all program code
def main():
    # dictionary with all rooms, directions, and items
    rooms = {
            'Dining Room': {'North': 'Kitchen', 'West': 'Patio', 'South': 'Exercise Room', 'East': 'Game Room'},
            'Kitchen': {'East': 'Garden', 'South': 'Dining Room', 'Item': 'Water'},
            'Garden': {'West': 'Kitchen', 'Item': 'Fruits/veggies'},
            'Patio': {'East': 'Dining Room', 'Item': 'Sun'},
            'Exercise Room': {'North': 'Dining Room', 'East': 'Bedroom', 'Item': 'Exercise'},
            'Bedroom': {'West': 'Exercise Room', 'Item': 'Sleep'},
            'Game Room': {'West': 'Dining Room', 'North': 'Basement', 'Item': 'Happiness'},
            'Basement': {'South': 'Game Room', 'Item': 'Poor Health'}
        }

    # set current room to Dining Room
    currentRoom = 'Dining Room'

    # set inventory variable to empty list
    inventory = []

    # status function has currentRoom as a parameter
    # prints what room the user is in and prompts user to input a command
    # also checks to see if player is in the basement or won the game
    def status(room, items):
        # check if player is in the basement, thus losing the game
        if room == 'Basement':
            print(f'\nYou are in the {room}')
            print(f'Inventory: {items}')
            print('-----------------------------')
            print('Poor health has consumed you, GAME OVER!'
                  '\nThank you for playing! Better luck next time :|')
            exit()

        # check if player collected all items, thus winning the game
        if len(items) == 6:
            print(f'\nYou are in the {room}')
            print(f'Inventory: {items}')
            print('-----------------------------')
            print('Congratulations! All items have been collected and you were'
                  '\nable to defeat poor health before it overtook your life!'
                  '\nThank you for playing the game! Hope you enjoyed it!')
            exit()

        # normal output after every command given
        print(f'\nYou are in the {room}')
        print(f'Inventory: {items}')

        # check to see if item key exists for the current room. If item key exists then checks to see if
        # item is in inventory or not, then prints the available item
        if 'Item' in rooms[room].keys():
            item = rooms[room]['Item']
            if item not in items:
                print(f'You see {item}')
        print('-----------------------------')

        # user input is automatically switched to lowercase for ease of use
        command = input('Enter your move:\n>').lower()
        return command

    # show_description function prints the storyboard description upon request and at the beginning of program
    def show_description():
        print('\n*****')
        print('Poor health is looming in your household, after making several unhealthy dietary decisions over the past'
              '\nfew months, due to working two jobs and taking on a bachelor’s degree program. You need to turn the'
              '\ntide before poor health consumes you. But before you battle poor health, there are some habits you'
              '\nmust pick up. You must get fresh fruits and vegetables from the garden to fortify your immune system,'
              '\nwater from the kitchen to stay hydrated, sun on the patio to get vitamin D, exercise in the exercise'
              '\nroom to strengthen your body and spirit and maintain a healthy weight, sleep in the bedroom for'
              '\nregeneration and healing, and finally happiness in the game room to help preserve your peace of mind.')
        print('*****')

    # show_instructions function prints main menu and commands
    def show_instructions():
        print("\n\nPoor Health Text Game")
        print("Collect 6 items to win the game, or be consumed by poor health...")
        print('**************************************************')
        print("Move commands: go South, go North, go East, go West")
        print("Add to Inventory: get 'item name' (ex. get 'happiness')")
        print("To see these instructions: main menu OR show instructions")
        print('To see description of game: show description')
        print('To go back the way you came: go back')
        print("To exit the game: exit")
        print('**************************************************')

    # get_items function contains validation and responses for get item command
    def get_items(room_item):
        nonlocal inventory
        nonlocal currentRoom

        # checks if item from command is already in inventory list
        if room_item in inventory:
            return 'Item already retrieved'

        # checks to see if item from command input matches item in the current room
        if room_item != rooms[currentRoom]['Item']:
            return f'{room_item} not available'

        # if item is valid, inventory list is updated with the item and retrieved response is printed
        inventory.append(room_item)
        return f'{room_item} retrieved!'

    # navigate function has status function's returned user input command as a parameter
    # moves the user from room to room or exits the game, depending on the valid command given
    def navigate(command):
        nonlocal currentRoom
        previous_room = []
        while currentRoom:
            # assign the dictionary value associated with the key matching the current room
            directions = rooms[currentRoom]

            # if command equals exit, loop is broken and game is ended
            if command == 'exit':
                print('Thank you for playing the game. Hope you enjoyed it. ')
                break

            # if command equals 'show instructions' or 'main menu' then instructions are printed to screen
            if command == 'show instructions' or command == 'main menu':
                show_instructions()
                command = status(currentRoom, inventory)
                continue

            # if command equals 'show description' then description of the game is printed to the screen
            if command == 'show description':
                show_description()
                command = status(currentRoom, inventory)
                continue

            # user input is split
            split_command = command.split()

            # if split command not equal to 2 or the first index of split_command not equal to get or go,
            # 'invalid move' message is printed
            if len(split_command) != 2 or split_command[0] not in ['go', 'get']:
                print('Invalid move!')
                command = status(currentRoom, inventory)
                continue

            # if the first index of split_command equals 'get', then the second index is sent to the get_items function
            # as a parameter for validation. Response from get_items is returned and printed
            if split_command[0] == 'get':
                retrieve = get_items(split_command[1].capitalize())
                print(retrieve)
                command = status(currentRoom, inventory)
                continue

            # variable direction is set to equal the second index of split_command with the first letter capitalized
            direction = split_command[1].capitalize()

            # allows player to go back and retrace their steps if 'back' is entered as second index in split_command
            if direction == 'Back':
                if len(previous_room) > 0:
                    currentRoom = previous_room.pop()
                    command = status(currentRoom, inventory)
                    continue
                else:
                    print('Unable to go back')
                    command = status(currentRoom, inventory)
                    continue

            # checks if direction is a key in the current room's set of directions
            if direction not in directions.keys():
                print('You can\'t go that way!')
                command = status(currentRoom, inventory)
                continue

            # update current room and prompt for new command
            previous_room.append(currentRoom)
            currentRoom = directions[direction.capitalize()]
            command = status(currentRoom, inventory)

    # function calls
    show_description()
    show_instructions()
    stat = status(currentRoom, inventory)
    navigate(stat)


main()
