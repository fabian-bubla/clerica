
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 20:42:29 2019


scroll function in pygame.surface for a screenshake
@author: fabia
"""


#%% CONSTANTS
FPS = 30
GBRES = (160, 144) #resolution of window
WIDTH, HEIGHT = GBRES[0], GBRES[1] #splits resolution in two variables WIDTH and HEIGHT

# PLAYER_ACC = 0.5
PLAYER_ACC = 0.35 #Player acceleration
PLAYER_FRICTION = -0.12 #player friction



GAMEBOY_FONT = {
    "file": "gameboy-font.png",
    "size": (7, 7)
    }

GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)


#%% TRIGGERS
start_screen_anim_index = 0
start_screen_count = 0
frame_counter = 0
last_frame_took_damage = 0
health_counter = 0
total_health = 1800 #frames needed to pass to win
start_anim_counter = 0
end_anim_counter = 0

#%% IMPORTS

import random, sys, pygame, os
from pygame.locals import *
vec = pygame.math.Vector2
import time

IMAGES = {}

def filepath(path):
    if "/" in path:
        path = path.split("/")
    elif "\\" in path:
        path = path.split("\\")
    if type(path) is type([]):
        return os.path.join(*path)
    else:
        return os.path.join(path)
def load_image(filename):
    if filename not in IMAGES:
        IMAGES[filename] = pygame.image.load(
            filepath(filename)).convert_alpha()
    return IMAGES[filename]



#%%IMAGES & ANIMATIONS

def load_animations():
    #### ALWAYS MAKE ALL OF THEM SHITTTY VARIABLES GLOBAL, I SHOULD HAVE NEVER MADE THIS A FUNCTION
    global background, clerica_walk_down, clerica_walk_left, clerica_walk_right, clerica_walk_up, clerica_idle, clerica_invincibility_frame
    global bird, bird_flipped, bunnybird, bunnybird_flipped
    global title_screen, end_screen, credits_screen, lose_screens, breathbar_overlay
    global clerica_hit
    background = load_image(r"Images\background\background0.png")
    clerica_walk_down = [load_image(r"Images\clerica\front\frontnormal0.png"), load_image(r"Images\clerica\front\frontnormal1.png")]
    
    clerica_walk_left = [load_image(r"Images\clerica\left\leftnormal0.png"), load_image(r"Images\clerica\left\leftnormal1.png")]

    clerica_walk_right = [load_image(r"Images\clerica\right\rightnormal0.png"), load_image(r"Images\clerica\right\rightnormal1.png")]
    
    clerica_walk_up = [load_image(r"Images\clerica\back\backnormal0.png"), load_image(r"Images\clerica\back\backnormal1.png")]
    
    clerica_idle = clerica_walk_down

    clerica_invincibility_frame = load_image(r"Images\clerica\invincibility_frame\clerica_invincibility_frame.png")
    bird = [load_image(r"Images\bird\bird0.png"), load_image(r"Images\bird\bird1.png")]

    bird_flipped = [load_image(r"Images\bird\bird_flipped0.png"), load_image(r"Images\bird\bird_flipped1.png")]

    bunnybird = [load_image(r"Images\bunnybird\bunnybird0.png"), load_image(r"Images\bunnybird\bunnybird1.png")]
    bunnybird_flipped = [load_image(r"Images\bunnybird\bunnybird_flipped0.png"), load_image(r"Images\bunnybird\bunnybird_flipped1.png")]

    title_screen = [load_image(r"Images\titlescreen\TitleScreen1.png"), load_image(r"Images\titlescreen\TitleScreen2.png"), load_image(r"Images\titlescreen\TitleScreen3.png"), load_image(r"Images\titlescreen\TitleScreen4.png"), load_image(r"Images\titlescreen\TitleScreen5.png"), load_image(r"Images\titlescreen\TitleScreen6.png"), load_image(r"Images\titlescreen\TitleScreen7.png"), load_image(r"Images\titlescreen\TitleScreen8.png"), load_image(r"Images\titlescreen\TitleScreen9.png"), load_image(r"Images\titlescreen\TitleScreen10.png"), load_image(r"Images\titlescreen\TitleScreen11.png"), load_image(r"Images\titlescreen\TitleScreen12.png"), load_image(r"Images\titlescreen\TitleScreen13.png"), load_image(r"Images\titlescreen\TitleScreen14.png"), load_image(r"Images\titlescreen\TitleScreen15.png"), load_image(r"Images\titlescreen\TitleScreen16.png"), load_image(r"Images\titlescreen\TitleScreen17.png"), load_image(r"Images\titlescreen\TitleScreen18.png"), load_image(r"Images\titlescreen\TitleScreen19.png"), load_image(r"Images\titlescreen\TitleScreen20.png"), load_image(r"Images\titlescreen\TitleScreen21.png"), load_image(r"Images\titlescreen\TitleScreen22.png"), load_image(r"Images\titlescreen\TitleScreen23.png"), load_image(r"Images\titlescreen\TitleScreen24.png"), load_image(r"Images\titlescreen\TitleScreen25.png"), load_image(r"Images\titlescreen\TitleScreen26.png"), load_image(r"Images\titlescreen\TitleScreen27.png"), load_image(r"Images\titlescreen\TitleScreen28.png"), load_image(r"Images\titlescreen\TitleScreen29.png"), load_image(r"Images\titlescreen\TitleScreen30.png"), load_image(r"Images\titlescreen\TitleScreen31.png"), load_image(r"Images\titlescreen\TitleScreen32.png"), load_image(r"Images\titlescreen\TitleScreen33.png"), load_image(r"Images\titlescreen\TitleScreen34.png"), load_image(r"Images\titlescreen\TitleScreen35.png"), load_image(r"Images\titlescreen\TitleScreen36.png"), load_image(r"Images\titlescreen\TitleScreen37.png"), load_image(r"Images\titlescreen\TitleScreen38.png"), load_image(r"Images\titlescreen\TitleScreen39.png"), load_image(r"Images\titlescreen\TitleScreen40.png"), load_image(r"Images\titlescreen\TitleScreen41.png"), load_image(r"Images\titlescreen\TitleScreen42.png"), load_image(r"Images\titlescreen\TitleScreen43.png"), load_image(r"Images\titlescreen\TitleScreen44.png"), load_image(r"Images\titlescreen\TitleScreen45.png"), load_image(r"Images\titlescreen\TitleScreen46.png"), load_image(r"Images\titlescreen\TitleScreen47.png"), load_image(r"Images\titlescreen\TitleScreen48.png")]

    end_screen = [load_image(r"Images\buddhascreen\buddhaface.png"), load_image(r"Images\buddhascreen\buddhahand.png"), load_image(r"Images\buddhascreen\buddhablush.png"), load_image(r"Images\buddhascreen\BuddhaScreen04.png")]
    credits_screen = load_image(r"Images\creditsscreen\CreditsScreen0.png")
    breathbar_overlay = load_image(r"Images\background\breathbaroverlay.png")
    lose_screens = [load_image(r"Images\lose_screens\quote0.png"), load_image(r"Images\lose_screens\quote1.png"), load_image(r"Images\lose_screens\quote2.png"), load_image(r"Images\lose_screens\quote3.png"), load_image(r"Images\lose_screens\quote4.png"), load_image(r"Images\lose_screens\quote5.png"), load_image(r"Images\lose_screens\quote6.png"), load_image(r"Images\lose_screens\quote7.png")]
    clerica_hit = [ load_image(r"Images\clerica\left\lefthit0.png"), load_image(r"Images\clerica\right\righthit0.png"), load_image(r"Images\clerica\front\fronthit0.png"), load_image(r"Images\clerica\back\backhit0.png")]

#%%SOUNDS
def load_sounds():
    global bird_sound, bomb_sound, death_sound, egg_sound, hit_sound, mole_sound,start_sound, fatbird_sound, enlightenment_sound
    bird_sound = pygame.mixer.Sound(r"sfx\bird1.wav")
    bird_sound.set_volume(0.08)
    bomb_sound = pygame.mixer.Sound(r"sfx\bomb.wav")
    death_sound = pygame.mixer.Sound(r"sfx\death.wav")
    egg_sound = pygame.mixer.Sound(r"sfx\egg.wav")
    hit_sound = pygame.mixer.Sound(r"sfx\hit.wav")
    hit_sound.set_volume(0.2)
    mole_sound = pygame.mixer.Sound(r"sfx\mole.wav")
    start_sound = pygame.mixer.Sound(r"sfx\start.wav")
    start_sound.set_volume(0.2)
    fatbird_sound = pygame.mixer.Sound(r"sfx\fatbird1.wav")
    enlightenment_sound = pygame.mixer.Sound(r"sfx\enlightenment.wav")

    #%% BASIC FUNCTIONS FOR INITIALIZATIONS
def init(scale=4.0, caption="Clerica", res=GBRES):
    """Initialise the SDL display -> return None
    """

    global SCALE, DISPLAYSURF, surface, resolution
    resolution = res
    SCALE = scale
    
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    
    pygame.display.set_caption(caption)
    # LOAD ICON PLACEHOLDER  https://stackoverflow.com/questions/21271059/how-do-i-change-the-pygame-icon

    DISPLAYSURF = pygame.display.set_mode((   #equivalent to DISPLAYSURF
        int(resolution[0]*SCALE),
        int(resolution[1]*SCALE)))  #add: , pygame.FULLSCREEN or pygame.RESIZABLE
    # icon = pygame.image.load(r"Images\background\birdicon.png").convert_alpha()
    # pygame.display.set_icon(icon)                                                    #However I am not sure if it works with the SCALE parameter
    surface = pygame.Surface(GBRES) #creates a surface in the GB resolution
    pygame.display.update()

    pygame.mouse.set_visible(0)

    print(pygame.display.Info())

def update():
    """Update and draw the scene -> return None
    """
    
    global surface, resolution
    surface = pygame.transform.scale(surface, 
        (int(resolution[0]*SCALE), int(resolution[1]*SCALE)))
    DISPLAYSURF.blit(surface, (0, 0))
    surface = pygame.transform.scale(surface, resolution)

    pygame.display.flip()

def get_surface():
    """Get the surface to draw to -> return pygame.Surface
    """
    
    return surface


# def gb_font_init():
#     global gb_font
#     gb_font = font.Font(GAMEBOY_FONT, (255, 255, 255)) #create the font


#%% OBJECTS
class Velocity_Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(r"Images\clerica\front\frontnormal0.png")
        self.images = clerica_idle
        self.image = self.images[0]

        self.anim_index = 0
        self.anim_timer = 0
        self.count = 0
        self.frame_keep = 4

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2) #tells where the center of the rectangle should be
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.hidden = False
        self.hide_timer = 1000

        self.counter = 0

    def hide(self):
            self.hidden = True
            self.hide_timer = pygame.time.get_ticks()



    def update(self):
        self.acc = vec(0, 0) #if no button is pressed, this is the velocity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            self.images = clerica_walk_left
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            self.images = clerica_walk_right
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.acc.y = -PLAYER_ACC
            self.images = clerica_walk_up
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.acc.y = PLAYER_ACC
            self.images = clerica_walk_down

        #APPLY FRICTION
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x >= WIDTH - int(self.rect.width/2)-2:
            self.pos.x = WIDTH - int(self.rect.width/2)-2
            self.vel.x = 0
        if self.pos.x <= 0 + int(self.rect.width/2) + 2:
            self.pos.x = 0 + int(self.rect.width/2) + 2
            self.vel.x = 0

        if self.pos.y >= HEIGHT - int(self.rect.height/2) -6:
            self.pos.y = HEIGHT - int(self.rect.height/2) - 6
            self.vel.y = 0

        # if self.pos.y <= 0 + int(self.rect.height/2):
        #     self.pos.y = 0 + int(self.rect.height/2)
        #     self.vel.y = 0
        #UPPER BOUNDARY
        if self.pos.y <= 24 + int(self.rect.height/2) +2:
            self.pos.y = 24 + int(self.rect.height/2) +2
            self.vel.y = 0


        self.rect.center = self.pos #i think updates the rect
        self.vx,self.vy = self.rect.topleft[0],self.rect.topleft[1]  #this just gives the top left corner position for the picture to render at with each update, so that this code has the same rendering as the non velocity code

        self.animate(dt, self.frame_keep)

        # #as long as
        # if self.hidden:
        #     self.frame_keep = 8
        #     if self.counter == 1:
        #         # self.frame_keep = 1
        #         self.image = clerica_invincibility_frame
        #         self.counter = 0
        #         # self.frame_keep = 2
        #         print('1')
        #     else:
        #         self.counter = 1
        #         self.framekeep = 4
        #         print('2')
        if self.hidden:
            if self.images == clerica_walk_left:
                self.image = clerica_hit[0]
            if self.images == clerica_walk_right:
                self.image = clerica_hit[1]
            if self.images == clerica_walk_down:
                self.image = clerica_hit[2]
            if self.images == clerica_walk_up:
                self.image = clerica_hit[3]


        #as long as
        # if self.hidden:
        #     self.frame_keep = 4
        #     if self.counter == 2:
        #         # self.frame_keep = 1
        #         # self.image = clerica_invincibility_frame
        #         self.counter = 0
        #         # self.frame_keep = 2
        #         print('1')
        #     else:
        #         self.counter += 1
        #         self.framekeep = 4
        #         print('2')

        if self.hidden and frame_counter - last_frame_took_damage > 60:
            self.hidden = False
            self.frame_keep = 4





        surface.blit(self.image, (self.vx, self.vy))

    def animate (self, dt, frame_keep):
        #add delta time to the anim_timer and increment index after 70s
        self.anim_timer += dt
        if self.anim_timer > .07:
            self.count += 1
            self.anim_timer = 0
            if self.count == frame_keep:
                self.count = 0
                self.anim_index +=1
                self.anim_index %= len(self.images)
                self.image = self.images[self.anim_index]







#%% MAIN LOOP

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        #SPRITE
        pygame.sprite.Sprite.__init__(self)

        if random.getrandbits(1):
            self.is_flipped = True
            self.images = bird_flipped #needs new sprites
        else:
            self.images = bird
            self.is_flipped = False
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        # SPEED
        self.vx = random.randrange(1, 3)   #moving speed
        self.vy = 0
        self.dy = 0.5   #necessary for the sine wave movement

        #SPAWN AREA
        if self.is_flipped == True:
            self.rect.centerx = -30
        elif self.is_flipped == False:
            self.rect.centerx = WIDTH + 30
            self.vx *= -1

        # self.rect.centerx = random.choice([-30, WIDTH + 30])
        self.rect.centery = random.randint(0 + HEIGHT/6, HEIGHT - 5)


        # ANIMATION COUNTERS
        self.anim_index = 0
        self.anim_timer = 0
        self.count = 0

    def update(self):
        #MOVING THE RECT
        self.rect.x += self.vx
        self.rect.y += self.vy
        #CALL ANIMATE
        self.animate(dt, 4)
        #BLIT
        surface.blit(self.image, self.rect)

        if self.rect.left > WIDTH + 30 or self.rect.right < -30:
            self.kill()

    def animate (self, dt, frame_keep):
        #add delta time to the anim_timer and increment index after 70s
        self.anim_timer += dt
        if self.anim_timer > .07:
            self.count += 1
            self.anim_timer = 0
            if self.count == frame_keep:
                self.count = 0
                self.anim_index +=1
                self.anim_index %= len(self.images)
                self.image = self.images[self.anim_index]

class Bunnybird(pygame.sprite.Sprite):
    def __init__(self):
        #SPRITE
        pygame.sprite.Sprite.__init__(self)
        if random.getrandbits(1):
            self.is_flipped = True
            self.images = bunnybird_flipped
        else:
            self.images = bunnybird
            self.is_flipped = False
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        # SPEED
        self.vx = random.randrange(1, 4)   #moving speed
        self.vy = 0
        self.dy = 0.5   #necessary for the sine wave movement

        #SPAWN AREA
        if self.is_flipped == True:
            self.rect.centerx = -30
        elif self.is_flipped == False:
            self.rect.centerx = WIDTH + 30
            self.vx *= -1

        # self.rect.centerx = random.choice([-30, WIDTH + 30])
        self.rect.centery = random.randint(0 + HEIGHT/6, HEIGHT - 5)


        # ANIMATION COUNTERS
        self.anim_index = 0
        self.anim_timer = 0
        self.count = 0

    def update(self):
        #MOVING THE RECT
        self.rect.x += self.vx
        self.rect.y += self.vy

        # BUNNYBIRD SINE MOVEMENT
        self.vy += self.dy
        if self.vy > 3 or self.vy < -3:  #the outer boundaries of the sine wave movement of the bird
            self.dy *= -1
        center = self.rect.center

        #CALL ANIMATE
        self.animate(dt, 4)
        #BLIT
        surface.blit(self.image, self.rect)

        if self.rect.left > WIDTH + 30 or self.rect.right < -30:
            self.kill()

    def animate (self, dt, frame_keep):
        #add delta time to the anim_timer and increment index after 70s
        self.anim_timer += dt
        if self.anim_timer > .07:
            self.count += 1
            self.anim_timer = 0
            if self.count == frame_keep:
                self.count = 0
                self.anim_index +=1
                self.anim_index %= len(self.images)
                self.image = self.images[self.anim_index]

class Mob_template(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = None
        self.image = None
        self.rect = self.image.get_rect() #get the rectangle around the sprite
        self.vx = None
        self.vy = None

    def update(self):
        #moves the rectangle according to the speed.
        self.rect.x += self.vx
        self.rect.y += self.vy

        animate(dt) #this should spit out a new self.image
        if None == True: #something about leaving or colliding
            self.image = None #should be the death image of foe if there is one.
            self.kill()
        surface.blit(self.image, self.rect)

    def animate (self, dt):
        #add delta time to the anim_timer and increment index after 70s
        self.anim_timer += dt
        if self.anim_timer > .07:
            self.count += 1
            self.anim_timer = 0
            if self.count == 4:
                self.count = 0
                self.anim_index +=1
                self.anim_index %= len(self.images)
                self.image = self.images[self.anim_index]


#%% MAIN LOOP

# def spawner(enemy, sprite_group, maxamount, time, variability):
#     global spawn_timer, all_sprites, mobs, birds
#     if pygame.time.get_ticks() - spawn_timer > random.randint(-variability, variability) + time:
#         spawn_timer = pygame.time.get_ticks()
#         for i in range(maxamount - len(sprite_group)):
#             m = enemy()
#             if enemy == Bird:
#                 birds.add(m)
#             if enemy == Bunnybird:
#                 bunnybirds.add(m)

class start_screen:

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        self.images = title_screen
        self.image = self.images[0]
        self.rect = self.image.get_rect() #get the rectangle around the sprite
    
        self.count = 0
        self.anim_index = 0
        self.anim_timer = 0
        self.show_start = True
    def update(self):
        pygame.time.Clock().tick(30)
        dt = FPSCLOCK.tick(FPS)/1000
        while self.show_start == True:
            #this should spit out a new self.image
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                show_start = False
            self.animate(dt)
            surface.blit(self.image, (0,0))
            if show_start == False:
                break

    def animate (self, dt):
        #add delta time to the anim_timer and increment index after 70s
        self.anim_timer += dt
        if self.anim_timer > .07:
            self.count += 1
            self.anim_timer = 0
            if self.count == 4:
                self.count = 0
                self.anim_index +=1
                self.anim_index %= len(self.images)
                self.image = self.images[self.anim_index]


def show_end_screen():
    enlightenment_sound.play()
    surface.blit(end_screen[0], (0,0))
    update()
    time.sleep(1)
    surface.blit(end_screen[1], (0,0))
    update()
    time.sleep(1)
    surface.blit(end_screen[2], (0,0))
    update()
    time.sleep(0.5)
    wait_for_key()
    pygame.mixer.music.load(r".\music\title_credits.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    surface.blit(credits_screen, (0,0))
    update()
    time.sleep(2)
    wait_for_key()
    pygame.quit()
    sys.exit()

def show_lose_screen():
    death_sound.play()
    surface.blit(lose_screens[random.randint(0,7)], (0,0))
    update()
    time.sleep(2)
    wait_for_key()
    pygame.quit()
    sys.exit()

def show_start_screen():
    # game splash/start screen
    pygame.mixer.music.load(r".\music\title_credits.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    surface.blit(title_screen[0], (0,0))
    update()
    wait_for_key_animated()

def wait_for_key_animated():
    global start_anim_counter
    waiting = True
    while waiting:
        pygame.time.Clock().tick(FPS)
        surface.blit(title_screen[start_anim_counter//3], (0,0))
        start_anim_counter += 1
        if start_anim_counter == 141:
            surface.blit(title_screen[start_anim_counter//3], (0,0))
            start_anim_counter = 0
        update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            if event.type == pygame.KEYUP:
                waiting = False

def wait_for_key():
    waiting = True
    while waiting:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            if event.type == pygame.KEYUP:
                waiting = False

def total_spawn_adapt_to_bar(maxamount):
    if maxamount * bar_percentage < 1:
        monster_amount = 1
    else:
        monster_amount = int(maxamount * bar_percentage * 2)  #the 2 is here because the int() always rounds it down so with a percentage you'd barely ever get an increase in the amount of mobs.
    return monster_amount
# def start_screen_animate():
#             start_screen_count += 1
#             if start_screen_count == 3:
#                 start_screen_count = 0
#                 start_screen_anim_index +=1
#                 start_screen_anim_index %= len(self.images)
#                 return start_screen_anim_index
def bar_mechanic():
    global bar_percentage
    bar_percentage = health_counter/total_health
    return bar_percentage

def _breathbar():
    global breathbar_overlay
    width = int(bar_percentage*112) #112 is because the percentage is based on 100s but the bar is 112 pixels
    color = (143, 187, 175) #bar color
    if width == 0: #fixes a bug where the bar is outside where it should be
        width = 1
    if width < 0:
        width = 1
        color = (214, 248, 184)
    breathbar_rect = Rect(24, 8, width, 8)
    pygame.draw.rect(surface, color, breathbar_rect)
    surface.blit(breathbar_overlay, (0,0))

def main():
    # INITIALIZATIONS
    global FPSCLOCK, dt, spawn_timer, mobs, frame_counter, health_counter, last_frame_took_damage
    FPSCLOCK = pygame.time.Clock()
    pygame.mixer.init()
    load_sounds()
    spawn_timer = pygame.time.get_ticks()
    init()
    load_animations()

    # gb_font_init()

    show_start_screen()
    start_sound.play()



    #Sprite Groups
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    birds = pygame.sprite.Group()
    bunnybirds = pygame.sprite.Group()

    #Player
    Clerica = Velocity_Player()
    all_sprites.add(Clerica)

    #Music Mixer
    pygame.mixer.music.load(os.path.join(r".\music\maintheme.mp3"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)


    #main loop

    while True:
        frame_counter +=1
        health_counter +=1
        dt = FPSCLOCK.tick(FPS) / 1000
        bar_mechanic()
        # spawner(Bird, birds, 2, 3, 1)
        # spawner(Bunnybird, bunnybirds, 2, 3, 1)
        maxamount, time, variability = 2, 2, 1
        if pygame.time.get_ticks() - spawn_timer > random.randint(-variability, variability) + time:
            for i in range(total_spawn_adapt_to_bar(maxamount) - len(birds)):
                m = Bird()
                birds.add(m)
                mobs.add(m)
                bird_sound.play()
                # print('bird')

        maxamount, time, variability = 2, 1, 1
        if pygame.time.get_ticks() - spawn_timer > random.randint(-variability, variability) + time:
            spawn_timer = pygame.time.get_ticks()
            for i in range(total_spawn_adapt_to_bar(maxamount) - len(bunnybirds)):
                m = Bunnybird()
                bunnybirds.add(m)
                mobs.add(m)
                bird_sound.play()

                # print('bunnybird')

        #UPDATES AND BLITS
        surface.blit(background, (0,0))
        _breathbar()
        mobs.update()
        Clerica.update()



        #COLLISIONCHECK
        hits = pygame.sprite.spritecollide(Clerica, mobs, False, pygame.sprite.collide_rect_ratio(0.1)) #makes a list with all the mobs that hit me
        for hit in hits:
            if frame_counter - last_frame_took_damage > 60: #90 frames need to pass to stop being invincible
                health_counter -= 200
                last_frame_took_damage = frame_counter #last frame of taking damage
                hit_sound.play()
            else:
                hit_sound.play()
                Clerica.hide()
                pass
            print(hitbox.__call__())



        #EVENTCHECK
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        update()
        
        if bar_percentage >= 1:
            show_end_screen()

        if bar_percentage <= 0:
            show_lose_screen()

if __name__.endswith('__main__'):
    main()






#%%STORAGE

# class Player (pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = load_image(r"Images\clerica\front\frontnormal0.png")
#         # self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.vx = 0
#         self.vy = 0

#     def update(self):
#         # self.vx = 0
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_a] or keys[pygame.K_LEFT]:
#             self.vx += -5
#             print('left')
#         if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
#             self.vx += 5
#             print ('right')
#         if keys[pygame.K_w] or keys[pygame.K_UP]:
#             self.vy += -5
#             print ('up')
#         if keys[pygame.K_s] or keys[pygame.K_DOWN]:
#             self.vy += 5
#             print ('down')
#         self.rect.x +=self.vx
#         self.rect.y +=self.vy



# class Title_Screen(object):
#     def __init__(self):
#         self.screen_stay = True
#         self.images = title_screen
#         self.frame_keep = 3
#         self.update()
#         sel
#     def update(self):
#         while self.screen_stay:
#             self.animate()
#             keys = pygame.key.get_pressed()
#             if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
#                 self.screen_stay = False

#     def animate (self, frame_keep):
#         #add delta time to the anim_timer and increment index after 70s
#         # self.anim_timer += dt
#         # if self.anim_timer > .07:
#             self.count += 1
#             # self.anim_timer = 0
#             if self.count == frame_keep:
#                 self.count = 0
#                 self.anim_index +=1
#                 self.anim_index %= len(self.images)
#                 self.image = self.images[self.anim_index]
