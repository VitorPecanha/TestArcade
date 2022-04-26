import arcade
import pathlib
#* Constants and windows dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650
SCREE_TITLE = "Test Game"

#* Assest path
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"

class Plataformer(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_HEIGHT, SCREEN_WIDTH, SCREE_TITLE)

        #Setup of different configs in the game
        self.coins = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        self.enemies = None
        self.player = None

        #Physic engine
        self.physics_engine = None

        #Score
        self.score = 0

        #Level
        self.level = 1

        #Assets parts
        # Load up our sounds here

        self.coin_sound = arcade.load_sound(

            str(ASSETS_PATH / "sounds" / "coin.wav")

        )

        self.jump_sound = arcade.load_sound(

            str(ASSETS_PATH / "sounds" / "jump.wav")

        )

        self.victory_sound = arcade.load_sound(

            str(ASSETS_PATH / "sounds" / "victory.wav")

        )

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
        """Draws the game"""
        pass

if __name__ == "__main__":
    window = Plataformer()
    window.setup()
    arcade.run()
    