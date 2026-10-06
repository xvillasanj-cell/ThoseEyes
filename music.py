import os
import sys
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def play_lyrics_with_image():
    pygame.init()
    pygame.mixer.init()

    
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Those Eyes - New West")

   
    image = pygame.image.load("picture.jpg")
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    
    pygame.mixer.music.load("thoseeyes.mp3")

    
    font = pygame.font.SysFont("Arial", 26, bold=True)

    lyrics_timeline = [
        (1.5, [
            ("'Cause ", 0.3), ("all ", 0.3), ("of ", 0.2), ("the ", 0.2), 
            ("small ", 1.1), ("things ", 1.8), ("that ", 0.3), ("you ", 0.3), ("do", 0.3)
        ]),
        (7.8, [
            ("Are ", 0.2), ("what ", 0.3), ("remind ", 0.9), ("me ", 0.4), 
            ("why ", 1.1), ("I ", 0.2), ("fell ", 0.6), ("for ", 0.3), ("you", 0.3)
        ]),
        (12.8, [
            ("And ", 0.2), ("when ", 0.3), ("we're ", 0.3), ("apart ", 0.9), 
            ("and ", 1.3), ("I'm ", 1.0), ("missing ", 0.7), ("you", 0.3)
        ]),
        (19.2, [
            ("I ", 0.2), ("close ", 0.4), ("my ", 0.3), ("eyes ", 0.9), 
            ("and ", 1.1), ("all ", 0.3), ("I ", 0.2), ("see ", 0.6), ("is ", 0.2), ("you", 0.3)
        ]),
        (24.5, [
            ("And ", 1.1), ("the ", 0.2), ("small ", 0.9), ("things ", 0.5), 
            ("you ", 0.8), ("do...", 0.1)
        ])
    ]

    pygame.mixer.music.play()
    start_time = time.time()

    line_index = 0
    word_index = 0
    current_displayed_text = ""
    word_start_time = None

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        elapsed_time = time.time() - start_time

       
        if line_index < len(lyrics_timeline):
            line_start, words = lyrics_timeline[line_index]
            
            if elapsed_time >= line_start:
                if word_index < len(words):
                    word_text, word_dur = words[word_index]
                    
                    if word_start_time is None:
                        word_start_time = elapsed_time

                    time_in_word = elapsed_time - word_start_time
                    chars_to_show = int((time_in_word / word_dur) * len(word_text)) + 1
                    
                    if chars_to_show >= len(word_text):
                        current_displayed_text += word_text
                        word_index += 1
                        word_start_time = None
                    else:
                        temp_text = current_displayed_text + word_text[:chars_to_show]
                else:
                    temp_text = current_displayed_text
            else:
                temp_text = ""
        else:
            temp_text = current_displayed_text


        if line_index < len(lyrics_timeline):
            if word_index >= len(lyrics_timeline[line_index][1]):
                if line_index + 1 < len(lyrics_timeline):
                    next_line_start = lyrics_timeline[line_index + 1][0]
                    if elapsed_time >= next_line_start:
                        line_index += 1
                        word_index = 0
                        current_displayed_text = ""

    
        screen.blit(image, (0, 0))

        overlay = pygame.Surface((WIDTH, 90))
        overlay.set_alpha(170)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, HEIGHT - 110))

        
        display_str = temp_text if 'temp_text' in locals() else current_displayed_text
        if display_str:
            text_surface = font.render(display_str, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 65))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    play_lyrics_with_image()