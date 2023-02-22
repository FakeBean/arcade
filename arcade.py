
import arcade
import random
 
class Bubble:
    def __init__(self, x, y ,speed_x, speed_y, size, colour) -> None:
        self.x = x
        self.y = y
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.size = size
        self.colour = colour
        
    def update(self):  
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x <= 0:
            self.speed_x = random.randint(1,10) 
        if self.y <= 0:
            self.speed_y = random.randint(1,10) 
        if self.x >=800:
            self.speed_x = random.randint(1,10) 
        if self.y >= 800:
            self.speed_y = random.randint(1,10) 


    def draw(self) -> None:
        arcade.draw_square_filled(self.x, self.y, self.size, self.color)
            
        

class Game(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "Goose")
        arcade.set_background_color(arcade.color.GRAY)
        self.bubbles = [] 
        for i in range(10):
            bubble = Bubble(
                random.randint(0, 400),
                random.randint(200, 500),
                random.randint(40, 470),
                random.randint(560, 600),
                random.randint(305, 477),
                random.randint(503, 800),
                (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            )

            self.bubbles.append(Bubble)

        def on_draw(self) -> None:
            self.clear()   
            for Bubble in self.bubbles:
                Bubble.draw()


        def on_key_press(self, symbol: int, modifiers:int) -> None:
            arcade.exit()        
   


       


      
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(f"{x=}, {y=}")

    def on_update(self, delta_time: float):
        self.x += self.bubble_speed_x
        self.y += self.bubble_speed_y

        if self.bubble_x <= 50:
            self.bubble_speed_x = random.randint(1, 10)
        if self.bubble_y <= 50:
            self.bubble_speed_y = random.randint(1, 10)
        if self.bubble_x >= 750:
            self.bubble_speed_x =- random.randint(1, 10)
        if self.bubble_y >= 750:
            self.bubble_speed_y =- random.randint(1, 10)



# Make the cookie
# Only run the file if it's the main file
if __name__ == '__main__':
    game = Game()
    arcade.run()  
