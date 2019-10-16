"""
Code for teaching newcomers about python, via cloning agar.io

covers:
    variable declaration
    variable adjusting
    
    conditions
    while loops
    foor loops
    
    Function declaration
    Argument passsing
    
    the pygame module
    
    Object oriented programming(OOP):
        classes
        instances
        public attributes
        __init__
        self
        functions within objects
"""
import math
import pygame
pygame.init()

class variables():
    screen_width = 1280
    screen_height = 720
    
    map_width = 300
    map_height = 300
    
    frame_rate = 100
    screen_follow_lag = 5

class agario_screen():
    fps = 60
    screen_offset_x = 0
    screen_offset_y = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sprite_list = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        
    def create(self):
        self.image = pygame.display.set_mode([self.width, self.height])
        
    def caption(self, string):
        pygame.display.set_caption(string)
        
    def background(self, r, g, b):
        self.image.fill((r, g, b))
        
    def set_fps(self, fps):
        self.fps = fps
        
    def draw_localPlayer(self, player):
        player_pos_x = player.position_x
        player_pos_y = player.position_y
        
        position_to_draw_x = player_pos_x - self.screen_offset_x
        position_to_draw_y = player_pos_y - self.screen_offset_y
                
        pygame.draw.circle(self.image, (255,255,255), (int(position_to_draw_x), int(position_to_draw_y)), 10)
        
    def convert_map_to_screen(self, x, y):
        return (x - self.screen_offset_x, y - self.screen_offset_y)
        
    def draw_map(self, map):
        #step 1: draw border lines
        pygame.draw.line(self.image, (255,255,255), self.convert_map_to_screen(0, 0), self.convert_map_to_screen(map.size_x, 0))
        pygame.draw.line(self.image, (255,255,255), self.convert_map_to_screen(0, 0), self.convert_map_to_screen(0, map.size_y))
        pygame.draw.line(self.image, (255,255,255), self.convert_map_to_screen(0, map.size_y), self.convert_map_to_screen(map.size_x, map.size_y))
        pygame.draw.line(self.image, (255,255,255), self.convert_map_to_screen(map.size_x, 0), self.convert_map_to_screen(map.size_x, map.size_y))
        
        
    def render(self):
        self.sprite_list.draw(self.image)
        pygame.display.flip()
        self.clock.tick(self.fps)
        
        
    def get_mouse_distance(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = mouse_x - (self.width/2)
        mouse_y = mouse_y - (self.height/2)
        
        return math.sqrt(mouse_x**2 + mouse_y**2)
        
    def get_mouse_direction(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = mouse_x - (self.width/2)
        mouse_y = mouse_y - (self.height/2)
        
        distance = self.get_mouse_distance()
        
        if distance < 1:
            distance = 1
        
        return mouse_x/distance, mouse_y/distance    
        
    
class agario_player():
    movement_speed = 2
    score = 5
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        
class agario_map():
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        
vars = variables()

screen = agario_screen(vars.screen_width, vars.screen_height)
screen.create()
screen.caption("Hello!")
screen.set_fps(vars.frame_rate)

map = agario_map(vars.map_width, vars.map_height)

local_player = agario_player()

done = False
while not done:
    screen.background(0, 0, 0)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    mouse_dir_x, mouse_dir_y = screen.get_mouse_direction()
    mouse_distance = screen.get_mouse_distance()*10
    
    speed = mouse_distance
    if speed > local_player.movement_speed:
        speed = local_player.movement_speed
    
    local_player.position_x += mouse_dir_x * local_player.movement_speed
    local_player.position_y += mouse_dir_y * local_player.movement_speed
    
    if local_player.position_x < 0:
        local_player.position_x = 0
    if local_player.position_y < 0:
        local_player.position_y = 0
    if local_player.position_x > map.size_x:
        local_player.position_x = map.size_x
    if local_player.position_y > map.size_y:
        local_player.position_y = map.size_y
        
    
    screen.screen_offset_x = local_player.position_x - screen.width/2 - mouse_dir_x * vars.screen_follow_lag
    screen.screen_offset_y = local_player.position_y - screen.height/2 - mouse_dir_y * vars.screen_follow_lag
    
    screen.draw_map(map)
    
    screen.draw_localPlayer(local_player)


    screen.render()
 
pygame.quit()