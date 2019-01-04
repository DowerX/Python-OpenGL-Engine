from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import obj_loader as obj

from pyrr import Quaternion, Matrix44, Vector3
#import numpy as np


print("\n")


#Settings
dev = True
display = (800,600)

objects = []



def modify(object_id,pos,rot,scale):
                
    translation = Vector3()
    translation += pos
                
    scale = Vector3(scale)

    matrix = Matrix44.identity()
    matrix = matrix * Matrix44.from_translation(translation)
    matrix = matrix * Matrix44.from_scale(scale)

    i = 0
    for point in objects[object_id].vertices:
        v = Vector3(point)
        v = matrix * v
        point = [v.x,v.y,v.z]
        objects[object_id].vertices[i] = point
        i+=1

        
def Load_map(path):
    with open(path, "r") as m:
        for line in m:
            if "#" in line: continue
            
            if "object " in line:
                parts = line.split(" ")
                del(parts[0])
                
                objects.append(obj.load(parts[0]))


                #Transforming it by the given amount
                rot = [0,0,0]
                modify(len(objects)-1,[float(parts[1].split(",")[0]),float(parts[1].split(",")[1]), float(parts[1].split(",")[2])],rot,[float(parts[3].split(",")[0]),float(parts[3].split(",")[1]), float(parts[3].split(",")[2])])

                if dev:
                    print("INFO: Loaded object with name '" + objects[len(objects)-1].name + "' from path '" + parts[0] + "'. Its position in the world is '" + str([float(parts[1].split(",")[0]),float(parts[1].split(",")[1]), float(parts[1].split(",")[2])]) + "' and its rotaition is '" + str(rot) + "'.")

def Render(otd):
    glBegin(GL_TRIANGLES)
    for face in otd.faces:
        e = 0
        for vertex in face.vertices:
            glNormal3f(otd.normals[face.normals[e]][0],otd.normals[face.normals[e]][1],otd.normals[face.normals[e]][2])
            glVertex3fv(otd.vertices[vertex])
            
            e+=1
            if e >= 3:
                e = 0
    glEnd()
    
    
def Main():
    pygame.init()
    pygame.display.set_mode(display, HWSURFACE|OPENGL|DOUBLEBUF)
    pygame.display.set_caption("OpenGL engine test")

    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glEnable(GL_CULL_FACE)
    glEnable(GL_BLEND)

    gluPerspective(60, (display[0]/display[1]), 0.1, 20.0)
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

        glRotatef(1,0,1,0)
        
        pygame.display.flip()
        #pygame.time.wait(1)


Main()
