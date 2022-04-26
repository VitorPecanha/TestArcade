import arcade

class Plataformer(arcade.Window):
    def __init__(self):
        pass

    def setup(self):
        """Sets up the game for the current level"""
        pass

    def on_key_press(self, key: int, modifiers: int):
        """Processes key presses
        
            Arguments:
                key {int} --> which key was pressed
                modifiers {int} --> which modifiers were down at the time
        """
        pass
    
    def on_key_release(self, key: int, modifiers: int):
        """Processes key releases

            Arguments:
                key {int} --> which key was released
                modifiers {int} --> which modifers were down at the time
        """
        pass

    def on_update(self, delta_time: float):
        """Updates the position of all game objects

            Arguments:
                delta_time {float} --> time since last call
        """
        pass

    def on_draw(self):
        pass

if __name__ == "__main__":
    window = Plataformer()
    window.setup()
    arcade.run()
    