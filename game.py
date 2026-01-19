# Start App for Creating a Character in Game

# Define symbols for full and empty dots
full_dot = '●'
empty_dot = '○'

# Validate character name
def validate_name(name):
    # Check if name is a string
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    # Check if name is empty
    if len(name) == 0:
        return 'The character should have a name'
    
    # Check if name is too long
    if len(name) > 10:
        return 'The character name is too long'
    
    # Check if name contains spaces
    if " " in name:
        return 'The character name should not contain spaces'


# Validate stats using a for-loop
def validate_stats(strength, intelligence, charisma):
    stats = [strength, intelligence, charisma]  # Put all stats in a list
    
    # Check if all stats are integers
    for stat in stats:
        if not isinstance(stat, int):
            return 'All stats should be integers'
    
    # Check if any stat is less than 1
    for stat in stats:
        if stat < 1:
            return 'All stats should be no less than 1'
    
    # Check if any stat is greater than 4
    for stat in stats:
        if stat > 4:
            return 'All stats should be no more than 4'
    
    # Check if the total sum of stats is 7
    if sum(stats) != 7:
        return 'The character should start with 7 points'


# Create the dot representation for a stat
def create_dots(stat):
    return full_dot * stat + empty_dot * (10 - stat)


# Create the full character using loops for stats
def create_character(name, strength, intelligence, charisma):
    # Validate the name
    name_error = validate_name(name)
    if name_error:
        return name_error
    
    # Validate the stats
    stats_error = validate_stats(strength, intelligence, charisma)
    if stats_error:
        return stats_error
        ## Return the character sheet as a multi-line string
        # Each stat is displayed with full (●) and empty (○) dots
        # \n is used to create a new line for each stat
    return (
        f'{name}\n'
        f'STR {create_dots(strength)}\n'
        f'INT {create_dots(intelligence)}\n'
        f'CHA {create_dots(charisma)}'
    )
        