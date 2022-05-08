import sys
import pygame

def check_events(ship):
    """Обрабатывает собитие клавиши событие мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                """Переместить корабль в право"""
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
def update_screen(ai_settings, screen, ship):
    """Обновляет изображение на экране и отображает новое"""
    # При каждом переходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Отображает последниий отображаемый экран
    pygame.display.flip()