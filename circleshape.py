import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0 ,0)
        self.radius = radius        

    def draw(self, screen):
        # must be overridden
        pass
    
    def update(self, dt):
        # must be overridden
        pass
    
    def check_collisions(self, circle_shape):
        distance = self.position.distance_to(circle_shape.position)
        r1 = self.radius
        r2 = circle_shape.radius        
        return distance <= (r1 + r2)