import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, color="white", center=self.position, radius=self.radius, width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split1_vector = self.velocity.rotate(split_angle)
        split2_vector = self.velocity.rotate(-split_angle)

        new_astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_astroid1.velocity = split1_vector * 1.2
        new_astroid2.velocity = split2_vector * 1.2
