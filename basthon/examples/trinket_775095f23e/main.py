from pylab import *
import pygame

# Variabler
g = 10           # Tyngdeakselerasjon i m/s^2
l = 0.5          # Lengden av snora i m
m = 1            # Massen av pendelen i kg
slippvinkel = 60 # Slippvinkel i grader

# Slippvinkel og vinkelfart
theta0 = radians(slippvinkel) # Startslippvinkel i radianer/s
w0 = 0                        # Startvinkelfart

w = w0                        # Vinkelfart i radianer/s
theta = theta0                # Slippvinkel i radianer

# Startposisjon
x = l*sin(theta)
y = -l*cos(theta)

# Visualisering 1: Setter opp Pygame (dette kan du se bort fra)
pygame.init()
vindux = 640
vinduy = 640
vindu = pygame.display.set_mode((vindux,vinduy))
pygame.display.set_caption("Pendellaboratorium")
HVIT = (255,255,255) # RGB-koden for hvit
SVART = (0,0,0)      # RGB-koden for svart
vindu.fill(HVIT)

# Visualisering 2: Tegner pendel (dette kan du se bort fra)
vx2 =  int(vindux/2)        # x-posisjon til pendelen i vinduet
vy2 = int(vinduy/2)      # y-posisjon til pendelen i vinduet
pygame.draw.line(vindu,SVART,(vx2,1),(int(round(vx2*x+vx2)),-int(round(vinduy*y))))
pygame.draw.circle(vindu,SVART,(int(round(vx2*x+vx2)),-int(round(vinduy*y))),15)
pygame.display.update()

run = True
dt = 1E-3 # NB: Tidssteget påvirker simuleringa i Pygame, og dermed svingetida
while run:
    vindu.fill(HVIT)
    
    # Her er fysikken!
    G = -m*g/l*sin(theta) # Tyngdekraften
    F = G                 # Summen av krefter
    a = F/m               # Akselerasjon
    
    w = w0 + a*dt         # Ny fart (vinkelfart)
    theta = theta0 + w*dt # Ny vinkel
    
    x = l*sin(theta)      # Ny posisjon i x-retning
    y = -l*cos(theta)     # Ny posisjon i y-retning
    
    theta0 = theta
    w0 = w 

    # Visualisering 3: Oppdaterer pendelposisjon (dette kan du se bort fra)
    pygame.draw.line(vindu,SVART,(vx2,1),(int(round(vindux*x+vx2)) ,-int(round(vinduy*y))))
    pygame.draw.circle(vindu,SVART,(int(round(vindux*x+vx2)) ,-int(round(vinduy*y))),15)
    pygame.display.update()
    
    # Løkka nedenfor gjør at vi kan avslutte simuleringen ved å trykke på krysset
    for e in pygame.event.get():
       if e.type == pygame.QUIT:
           run = False
           pygame.quit()
