import cv2
import mediapipe as mp
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Monster Electro")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
darkcyan = (0, 139, 139)


# Helper functions
def dist(p1x, p1y, p2x, p2y):
    return math.sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)


class Segment:
    def __init__(self, parent, l, a, first):
        self.first = first
        if first:
            self.pos = {'x': parent['x'], 'y': parent['y']}
        else:
            self.pos = {'x': parent.nextPos['x'], 'y': parent.nextPos['y']}
        self.l = l
        self.ang = a
        self.nextPos = {
            'x': self.pos['x'] + self.l * math.cos(self.ang),
            'y': self.pos['y'] + self.l * math.sin(self.ang)
        }

    def update(self, t):
        self.ang = math.atan2(t['y'] - self.pos['y'], t['x'] - self.pos['x'])
        self.pos['x'] = t['x'] + self.l * math.cos(self.ang - math.pi)
        self.pos['y'] = t['y'] + self.l * math.sin(self.ang - math.pi)
        self.nextPos['x'] = self.pos['x'] + self.l * math.cos(self.ang)
        self.nextPos['y'] = self.pos['y'] + self.l * math.sin(self.ang)

    def fallback(self, t):
        self.pos['x'] = t['x']
        self.pos['y'] = t['y']
        self.nextPos['x'] = self.pos['x'] + self.l * math.cos(self.ang)
        self.nextPos['y'] = self.pos['y'] + self.l * math.sin(self.ang)

    def show(self, screen):
        pygame.draw.line(screen, white, (self.pos['x'], self.pos['y']), (self.nextPos['x'], self.nextPos['y']), 2)


class Tentacle:
    def __init__(self, x, y, l, n, a):
        self.x = x
        self.y = y
        self.l = l
        self.n = n
        self.t = {}
        self.rand = random.random()
        self.segments = [Segment({'x': self.x, 'y': self.y}, self.l / self.n, 0, True)]
        for i in range(1, self.n):
            self.segments.append(Segment(self.segments[i - 1], self.l / self.n, 0, False))

    def move(self, last_target, target):
        self.angle = math.atan2(target['y'] - self.y, target['x'] - self.x)
        self.dt = dist(last_target['x'], last_target['y'], target['x'], target['y']) + 5
        self.t = {
            'x': target['x'] - 0.8 * self.dt * math.cos(self.angle),
            'y': target['y'] - 0.8 * self.dt * math.sin(self.angle)
        }
        if self.t['x']:
            self.segments[self.n - 1].update(self.t)
        else:
            self.segments[self.n - 1].update(target)
        for i in range(self.n - 2, -1, -1):
            self.segments[i].update(self.segments[i + 1].pos)
        if dist(self.x, self.y, target['x'], target['y']) <= self.l + dist(last_target['x'], last_target['y'],
                                                                           target['x'], target['y']):
            self.segments[0].fallback({'x': self.x, 'y': self.y})
            for i in range(1, self.n):
                self.segments[i].fallback(self.segments[i - 1].nextPos)

    def show(self, screen, target):
        if dist(self.x, self.y, target['x'], target['y']) <= self.l:
            for segment in self.segments:
                segment.show(screen)

    def show2(self, screen, target):
        if dist(self.x, self.y, target['x'], target['y']) <= self.l:
            pygame.draw.circle(screen, white, (int(self.x), int(self.y)), 2 * int(self.rand) + 1)
        else:
            pygame.draw.circle(screen, darkcyan, (int(self.x), int(self.y)), int(self.rand) * 2)


# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    maxl = 300
    minl = 50
    n = 30
    numt = 500
    tent = []
    clicked = False
    target = {'x': width // 2, 'y': height // 2, 'errx': 0, 'erry': 0}
    last_target = target.copy()
    t = 0
    q = 10

    for i in range(numt):
        tent.append(
            Tentacle(random.random() * width, random.random() * height, random.random() * (maxl - minl) + minl, n,
                     random.random() * 2 * math.pi))

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                target['x'] = int(index_finger_tip.x * width)
                target['y'] = int(index_finger_tip.y * height)
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        screen.fill(black)

        target['errx'] = target['x'] - target['x']
        target['erry'] = target['y'] - target['y']

        target['x'] += target['errx'] / 10
        target['y'] += target['erry'] / 10

        t += 0.01

        pygame.draw.circle(screen, (210, 100, 80), (int(target['x']), int(target['y'])),
                           int(dist(last_target['x'], last_target['y'], target['x'], target['y'])) + 5)

        for tentacle in tent:
            tentacle.move(last_target, target)
            tentacle.show2(screen, target)
        for tentacle in tent:
            tentacle.show(screen, target)

        last_target = target.copy()

        pygame.display.flip()
        clock.tick(60)

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()


if __name__ == "__main__":
    main()
