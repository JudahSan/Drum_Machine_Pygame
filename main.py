# Beat Maker
from os import path
from secrets import randbelow
from telnetlib import DO
from matplotlib import colors
import pygame
from pygame import mixer

# intialize for fonts and other built in fuctionalities
pygame.init()
pygame.font.init()

# screen
WIDTH = 1400
HEIGHT = 800

# rgb colors
black = (0, 0, 0)
white = (255, 255, 255)
# ...and some shade of gray, maybe 50 of em "wink"
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (100,149,237)
dark_grey = (50, 50, 50)
slate_grey = (47,79,79)

# creating screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Builder')
label_font = pygame.font.Font('freesansbold.ttf', 32)
medium_font = pygame.font.Font('freesansbold.ttf', 25)


# frame rate
fps = 60
timer = pygame.time.Clock()
beats = 8
# rows
instruments = 6
boxes = []
# create a list of lists initially -1
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
active_channel = [1 for _ in range(instruments)]
bpm = 248
playing = True
active_length = 0
active_beat = 0
beat_change = True


# load in sounds

hi_hat = mixer.Sound('sounds/hi_hat.WAV')
snare = mixer.Sound('sounds/snare.WAV')
kick = mixer.Sound('sounds/kick.WAV')
crash = mixer.Sound('sounds/crash.wav')
clap = mixer.Sound('sounds/clap.wav')
tom = mixer.Sound('sounds//tom.WAV')
pygame.mixer.set_num_channels(instruments * 3)

def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_channel[i] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                tom.play()
            if i == 5:
                clap.play()
            

def draw_grid(clicks, beat, actives):
    # left menu
    boxes = []
    left_box = pygame.draw.rect(screen, gray, [0, 0, 220, HEIGHT - 200], 5)
    # bottom menu
    bottom_box = pygame.draw.rect(screen, gray,  [0, HEIGHT - 200, WIDTH, 200], 5)
    # TODO: drum kit
    
    for i in range(instruments + 1):
        pygame.draw.line(screen, gray, (0, (i*100)), (220,(i*100)), 3)
    colors = [gray, white, gray]
    # draw another screen
    # hi hat
    hi_hat_text = label_font.render('Hi Hat', True, colors[actives[0]])
    screen.blit(hi_hat_text, (30, 30))
    # snare
    snare_text = label_font.render('Snare', True, colors[actives[1]])
    screen.blit(snare_text, (30, 130))
    # kick drum
    bass_drum_text = label_font.render('Bass Drum', True, colors[actives[2]])
    screen.blit(bass_drum_text, (30, 230))
    # crash cymbal
    crash_text = label_font.render('Crash', True, colors[actives[3]])
    screen.blit(crash_text, (30, 330))
    # floor time
    floor_tom_text = label_font.render('Floor Tom', True, colors[actives[4]])
    screen.blit(floor_tom_text, (30, 430))
    # clap
    clap_text = label_font.render('Clap', True, colors[actives[5]])
    screen.blit(clap_text, (30, 530))
    # lines
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100),(200, (i * 100)+ 100), 3)

    # Check how many boxes we need to draw for each instrument
    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                if actives[j] == 1:
                    color = green
                else:
                    color = dark_grey
            rect = pygame.draw.rect(screen,color, 
                [i*((WIDTH-220)//beats) + 225, 
                (j*100) + 5, ((WIDTH-220)//beats) - 10,
                ((HEIGHT - 200)//instruments) ],
                0, 5)
            pygame.draw.rect(
                screen,
                gold, 
                [i*((WIDTH-220)//beats) + 220, 
                (j*100), ((WIDTH-220)//beats),
                ((HEIGHT - 200)//instruments)],
                5, 5)
            pygame.draw.rect(
                screen,
                black, 
                [i*((WIDTH-220)//beats) + 220, 
                (j*100), ((WIDTH-220)//beats),
                ((HEIGHT - 200)//instruments)],
                2, 5)
            # return rect of each beat plus an x,y coordinate for it
            boxes.append((rect, (i,j)))

    active = pygame.draw.rect(screen, blue,
                              [beat * ((WIDTH - 220) // beats) + 220, 0, ((WIDTH - 220) // beats), instruments * 100],
                              5, 3)

    return boxes

# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat, active_channel)

# (lower menu buttons )play pause
    play_pause = pygame.draw.rect(screen, gray, [50, HEIGHT - 150, 225, 100], 0, 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text, (70, HEIGHT - 130))
    if playing:
        play_text2 = medium_font.render("Playing", True, dark_grey)
    else:
        play_text2 = medium_font.render("Paused", True, dark_grey)
    screen.blit(play_text2, (70, HEIGHT - 100))
    # bpm
    bpm_rect = pygame.draw.rect(screen, gray, [300, HEIGHT - 150, 225, 120], 5, 5)
    bpm_text = medium_font.render('Beats per Minute', True, white)
    screen.blit(bpm_text, (308, HEIGHT - 130))
    bpm_text2 = label_font.render(f'{bpm}', True, white)
    screen.blit(bpm_text2, (370, HEIGHT - 100))
    bpm_add_rect = pygame.draw.rect(screen, gray, [530, HEIGHT - 150, 48, 48], 0, 5)
    bpm_sub_rect = pygame.draw.rect(screen, gray, [530, HEIGHT - 100, 48, 48], 0, 5)
    add_text = medium_font.render('+5', True, white)
    sub_text = medium_font.render('-5', True, white)
    screen.blit(add_text, (538, HEIGHT - 140))
    screen.blit(sub_text, (538, HEIGHT - 90))
    # beats manenos
    beats_rect = pygame.draw.rect(screen, gray, [600, HEIGHT - 150, 225, 120], 5, 5)
    beats_text = medium_font.render('Beats In Loop', True, white)
    screen.blit(beats_text, (608, HEIGHT - 130))
    beats_text2 = label_font.render(f'{beats}', True, white)
    screen.blit(beats_text2, (670, HEIGHT - 100))
    beats_add_rect = pygame.draw.rect(screen, gray, [830, HEIGHT - 150, 48, 48], 0, 5)
    beats_sub_rect = pygame.draw.rect(screen, gray, [830, HEIGHT - 100, 48, 48], 0, 5)
    add_text = medium_font.render('+1', True, white)
    sub_text = medium_font.render('-1', True, white)
    screen.blit(add_text, (838, HEIGHT - 140))
    screen.blit(sub_text, (838, HEIGHT - 90))
    # instrument rects
    instrument_rects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i * 100), (220, 100))
        instrument_rects.append(rect)


    if beat_change:
        play_notes()
        beat_change = False


    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if we clicled on the rect we defined
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True
            elif bpm_add_rect.collidepoint(event.pos):
                bpm += 5
            elif bpm_sub_rect.collidepoint(event.pos):
                bpm -= 5
            elif beats_add_rect.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beats_sub_rect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            for i in range(len(instrument_rects)):
                if instrument_rects[i].collidepoint(event.pos):
                    active_channel[i] *= -1
                
        
    # how long should each beat be
    # fps * 60 // bpm
    # floor division to get integer
    beat_length = 3600 // bpm

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat +=1
                beat_change = True
            else:
                active_beat = 0
                beat_change = True

    pygame.display.flip()
pygame.quit()