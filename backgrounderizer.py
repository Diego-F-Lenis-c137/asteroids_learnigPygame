import pygame
import math as m
import random as r


class Backgrounderizer():

    def __init__(self, resolution: tuple, screen):
        self.w = resolution[0]
        self.h = resolution[1]
        self.center = (resolution[0]//2, resolution[1]//2)
        self.n = 50
        self.frames_per_cycle = 1800  # Number of frames for complete 360° rotation (360° / 0.2°per frame)
        self.current_frame = 0

        self.angle       = 0.0
        self.angular_vel = 0.2
        self.stars = self.design()
        self.star_data = self.precalculate_star_data()
        self.surf = pygame.Surface((self.w, self.h))
        self.screen = screen    

    def design(self):
        stars = []
        for x in range(self.n):
            ang = r.randint(0, 360)
            pos = ((20*x*(m.cos(ang))), (20*x*(m.sin(ang))))
            pos = (pos[0] + self.w//2, pos[1] + self.h//2)
            # Precompute initial color
            r_val = abs(int(pos[0]) // 10)
            g_val = abs(int(pos[1]) // 10)
            b_val = (r_val + g_val) // 2
            color = (r_val, g_val, b_val)
            star = [pos, ang, x, color]  # [position, angle, radius_multiplier, color]
            
            stars.append(star)
        return stars
    
    def precalculate_star_data(self):
        """
        Pre-calculate all star positions and colors for each frame in the cycle.
        Returns a 2D array: [frame][star_index] = (x, y, color)
        """
        star_data = []
        
        # Calculate positions and colors for each frame in the cycle
        for frame in range(self.frames_per_cycle):
            frame_data = []
            
            # Calculate dt for this frame (assuming 60 FPS)
            dt = frame / 60.0  # Time elapsed since start
            
            for star in self.stars:
                initial_angle = star[1]  # Initial angle
                radius_mult = star[2]    # Radius multiplier
                
                # Calculate angle for this frame
                ang = (initial_angle + self.angular_vel * dt * 60) % 360  # *60 to convert dt back to frames
                
                # Calculate position
                pos_x = 20 * radius_mult * m.cos(m.radians(ang)) + self.w // 2
                pos_y = 20 * radius_mult * m.sin(m.radians(ang)) + self.h // 2
                
                # Calculate color based on position (same logic as original)
                r_val = abs(int(pos_x) // 10) + 50
                g_val = abs(int(pos_y) // 10) + 50
                b_val = ((r_val + g_val) // 2) + 50
                
                # Clamp values to 255
                r_val = min(r_val, 255)
                g_val = min(g_val, 255)
                b_val = min(b_val, 255)
                
                color = (r_val, g_val, b_val)
                
                frame_data.append((pos_x, pos_y, color))
            
            star_data.append(frame_data)
        
        return star_data

    def update(self, dt: float):
        """
        Update star positions and colors using pre-calculated values.
        """
        self.surf.fill((0, 0, 0))
        
        # Get data for current frame
        current_frame_data = self.star_data[self.current_frame]
        
        # Update star positions and colors from pre-calculated array
        for i, star in enumerate(self.stars):
            pos_x, pos_y, color = current_frame_data[i]
            star[0] = (pos_x, pos_y)  # Update position
            star[3] = color           # Update color
        
        # Move to next frame in cycle
        self.current_frame = (self.current_frame + 1) % self.frames_per_cycle

    def draw(self, dt: float):
        self.update(dt)
        for i in self.stars:
            x, y = int(i[0][0]), int(i[0][1])
            color = i[3] # index 3 for polar coordinates version
            # Apply the same random color variation as original
            color = r.choices([color, (255, 255, 255), (0,0,0)], weights=[0.8, 0.1, 0.01], k=1)[0]
            pygame.draw.rect(self.surf, color, (x, y, 3, 3))
        self.screen.blit(self.surf, (0, 0, self.w, self.h))
