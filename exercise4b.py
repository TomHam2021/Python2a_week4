'''
Description

In this exercise you will implement a Context Manger that can be used as a save
file for a game. Save files are a common implementation in the video game 
industry and have several usages such as saving settings, campaign progress, 
user info or changes in the game's layout. As the complexity can be immense 
depending on scale, a simple implementation will here be used to store the 
users' settings with their resolution, difficulty setting and their characters 
progression in terms of level, name and how many hot dogs the character have ate
so far.
Note: In this exercise we will use the class-based approach as detailed above.

Setup
• Create a class called Character with three attributes, self._level, self._name
  and self._trait. Also create a property method allattributes that returns all 
  the attributes formatted with newline between each (check example below)
• Create a class called Settings with two attributes, self._resolution and 
  self._difficulty. Also create a property method allsettings that returns 
  [self._resolution + "\n" + self._difficulty + "\n"]
• Create a context manager with the template above
  Note: Make these five attributes’ properties by giving each of the variables 
  a property method for retrieving their respective values, as discussed 
  previously in the course this is a good practice.

'''

# https://www.pythontutorial.net/advanced-python/python-context-managers/

# Method 4: Use the logging module
# https://www.askpython.com/python/built-in-methods/python-print-to-file


class MyFileContextManager:
    def __init__(self, filename, operation):
        self._file = open(filename, operation)

    def __enter__(self):
        return self._file

    def __exit__(self, type, value, traceback):
        self._file.close()


class Character:
    # Create a class called Character with three attributes, self._level, self._name and self._trait.
    # w = write = ny fil -> filen finns inte eller skrivs över
    def __init__(self, level, name, trait):
        self._level = level
        self._name = name
        self._trait = trait
        with MyFileContextManager("game_data.txt", 'w') as f:
            f.write("Attribute\n")
            f.write(str(self._level) + '\n')
            f.write(self._name + '\n')
            f.write(self._trait + '\n')
            f.write("-------------------------\n")

    # By default, if the method is not a static python method, then implicitly
    # the object (self) is passed as argument.
    def allattributes(self):
        # Also create a property method allattributes that returns all
        # the attributes formatted with newline between each (check example below)
        with MyFileContextManager("game_data.txt", 'r') as f:
            for row in f:
                print(row.strip())  # strip the newline character from the line


class Settings:
    # Create a class called Settings with two attributes, self._resolution and self._difficulty.
    # a = append , filen finns -> uppdateras, OBS att Character måste köras innan (skapa filen)
    def __init__(self, resolution, difficulty):
        self._resolution = resolution
        self._difficulty = difficulty
        with MyFileContextManager("game_data.txt", 'a') as f:
            f.write("Graphics\n")
            f.write(self._resolution + '\n')
            f.write(str(self._difficulty) + '\n')
            f.write("-------------------------\n")

    def allsettings(self):
        # Also create a property method allsettings that returns [self._resolution + "\n" + self._difficulty + "\n"]
        skipp = bool
        with MyFileContextManager("game_data.txt", 'r') as f:
            skipp = True
            for row in f:
                # hoppa fram i filen till Graphics..
                if skipp:
                    if row == "Graphics\n":
                        print(row.strip())
                        skipp = False
                else:
                    # strip the newline character from the line
                    print(row.strip())


'''
Tasks
• Create a character, set level and name to what you’d like and trait to 
  something that defines your character, for example I set mine to "dogtamer".
• Create an instance of the Settings, resolution should be a string such 
  as "1280x720" and difficulty in the range of 1-10
• Using the contextmanager and the allsettings and allattributes methods 
  write and create a file called saveFile.txt.
'''

# Create a character, set level and name to what you’d like and trait to
# something that defines your character,
Character01 = Character(10, "Char01", "atacker")
Character01.allattributes()

# Create an instance of the Settings, resolution should be a string such as
# "1280x720" and difficulty in the range of 1-10
Settings01 = Settings("1280x720", 5)
Settings01.allsettings()
# Using the contextmanager and the allsettings and allattributes methods
# write and create a file called saveFile.txt.
