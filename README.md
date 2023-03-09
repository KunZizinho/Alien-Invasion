# Alien-Invasion

    In Alien Invasion, the player controls a rocket ship that appears at the bottom of the screen.
    The player can move the ship right and left using arrow keys and shoot bullets using the spacebar.
    When the game begins, a fleet of aliens fills the sky and moves across and down the screen.
    The player shoots and destroy's aliens.
    If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet.
    If any alien hits the player's ship or reaches the bottom of the screen, 
    the player loses a ship. If the player loses three ships, the game ends.

# import sys and pygame modules
    Pygame module contains the functionality we need to make the game.
    The game starts as  a class called AlienInvasion.

# __init__() method and pygame.init() function
    In the __init__() method , the pygame.init() function initializes the background settings that pygame needs to work properly.
    Then we call pygame.display.set_mode() to create a display window, on which we 'll draw all the games graphical elements.
    The argument (1200, 800) is the tuple that defines  the dimensions of the game window, which will be 1200 px wide and 800px high.
    We then assign this display to the attribute self.screen, so it can be available in all the methods in the class.
    The object  we assigned to self.screen is called SURFACE.
    Surface in  pygame is a part of screen where  a game element will be displayed. Each element in the game is it's own surface, 
    but the surface returned by display.set_mode() represents the entire game window.

# run_game() method
    The game is controlled by the run_game() method. This method contains a while loop that runs contininually.
    The while loop contains an event  and code that manages screen updates. An event is an action that the user performs while playing the game, 
    such as pressing a key or moving the mouse. Within the run_game() method we have a for loop which is an event loop.
    To access the events that py game detects, we use pygame.event.get() function. This function returns a list of events that took placesince last time
    this function was called.
    For example , when player clicks  the game window's close button, a pygame.QUIT event is detected and we call sys.exit() to exit the game.
    To call to pygame.display.flip() tells pygame to most recent drawn screen visible. In this case draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is visible.

# Adding settings.py module and Class Settings
    Instead  of adding all of our settings throughout the code, we created a settings module with class Settings to store all these values in one place.
    This approach allows us to work wit only one settings object any time we need to access an individual setting.
    This also makesit easier to modify game's apperance and behavior as our project grow.

# Adding ship moddule 
    First we are gonna add images folder to our directory, and upload our artwork.
    We are gonna use pygame blit() method to draw the image of the ship.
    We are gonna use bmp. files bc pygame loads bmp. files by default.
    Then we are gonna create ship.py module with class Ship that's gonna manage most of ships behavior.
    
    