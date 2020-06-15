import pygame

class Sounds():
    """Create sounds during gameplay"""
    def __init__(self):

        #Sound files
        file_name_shoot = 'laser_shoot.wav'
        file_name_explosion = 'explosion.wav'
        file_name_end_sound = 'retro_explosion.wav'
        self.shooting = pygame.mixer.Sound(file_name_shoot)
        self.explosion = pygame.mixer.Sound(file_name_explosion)
        self.end_sound = pygame.mixer.Sound(file_name_end_sound)

    def play_shoot_sound(self):
        """Play shooting sounds"""
        pygame.mixer.Sound.play(self.shooting)

    def play_explosion_sound(self):
        """Play explosion sounds"""
        pygame.mixer.Sound.play(self.explosion)

    def play_end_sound(self):
        """Play end game sounds"""
        pygame.mixer.Sound.play(self.end_sound)



