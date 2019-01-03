from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import obj_loader as obj
#from pyrr import Quaternion, Matrix33, Matrix44, Vector3
#import numpy as np

print("\n")

#Settings
dev = True
display = (800,600)

objects = []

def Load_map(path):
    with open(path, "r") as m:
        for line in m:          
            if "model " in line:
                parts = line.split(" ")
                del(parts[0])
                objects.append(obj.load(parts[0]))

                if dev:
                    print("INFO: Loaded object with name '" + objects[len(objects)-1].name + "' from path '" + parts[0] + "'.")

def Render(otd):
    glBegin(GL_TRIANGLES)
    for face in otd.faces:
        for vertex in face.vertices:
            glVertex3fv(otd.vertices[vertex])

    glEnd()
    
def main():
    pygame.init()
    pygame.display.set_mode(display, HWSURFACE|OPENGL|DOUBLEBUF)
    pygame.display.set_caption("OpenGL engine test")
    clock = pygame.time.Clock()
    clock.tick(16)

    glEnable(GL_COLOR_MATERIAL)

    gluPerspective(60, (display[0]/display[1]), 0.1, 100.0)
    glTranslate(0.0,0.0,-5)

    Load_map("./maps/test.map")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #RENDER HERE
        for model in objects:
            Render(model)

        glRotatef(1,1,1,1)
        
        pygame.display.flip()
        pygame.time.wait(10)


main()
