from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import obj_loader as obj

from pyrr import Quaternion, Matrix44, Vector3
import numpy as np


print("\nOpenGL Python engine")


#Settings
dev = True          #Additional information in the console about things happening
display = (640,480) #Drawing image size

objects = []        #Contains all objects that had been loaded and can be drawn
buffers = []
ibos = []

def CreateBufferForObjects():

    i = 0
    for _object in objects:
        x = 0
        glGenBuffers(1,x)
        buffers.append(x)
        print("B: " + str(buffers))
        
        glGenBuffers(1,x)
        ibos.append(x)
        print("I: " + str(ibos))

        
        glBindBuffer(GL_ARRAY_BUFFER, buffers[i])
        glBufferData(GL_ARRAY_BUFFER, len(_object.vertices) * np.array(_object.vertices, dtype="float32").itemsize, np.array(_object.vertices, dtype="float32"), GL_STATIC_DRAW)
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE, 24 * 3, 0)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibos[i])
        glBufferData(GL_ARRAY_BUFFER, len(_object.order) * 24, _object.order, GL_STATIC_DRAW)
        

##def Modify(object_id,pos,rot,scale):
##                
##    translation = Vector3()
##    translation += pos
##                
##    scale = Vector3(scale)
##
##    matrix = Matrix44.identity()
##    matrix = matrix * Matrix44.from_translation(translation)
##    matrix = matrix * Matrix44.from_scale(scale)
##
##    i = 0
##    for point in objects[object_id].vertices:
##        v = Vector3(point)
##        v = matrix * v
##        point = [v.x,v.y,v.z]
##        objects[object_id].vertices[i] = point
##        i+=1

        
def Load_map(path):
    with open(path, "r") as m:
        for line in m:
            if "#" in line: continue
            
            if "object " in line:
                parts = line.split(" ")
                del(parts[0])
                
                objects.append(obj.load(parts[0]))

                rot = [0,0,0]
                #Modify(len(objects)-1,[float(parts[1].split(",")[0]),float(parts[1].split(",")[1]), float(parts[1].split(",")[2])],rot,[float(parts[3].split(",")[0]),float(parts[3].split(",")[1]), float(parts[3].split(",")[2])])

                #if dev:
                #    print("INFO: Loaded object with name '" + objects[len(objects)-1].name + "' from path '" + parts[0] + "'. Its position in the world is '" + str([float(parts[1].split(",")[0]),float(parts[1].split(",")[1]), float(parts[1].split(",")[2])]) + "' and its rotaition is '" + str(rot) + "'.")

def Render(index):
    glBindBuffer(buffers[index])
    glBindBuffer(ibos[index])
    glDrawElements(GL_TRIANGLES, len(objects[index].order), GL_UNSIGNED_INT, None)
    
    
def Main():
    #PyGame setup
    pygame.init()
    pygame.display.set_mode(display, HWSURFACE|OPENGL|DOUBLEBUF)
    pygame.display.set_caption("OpenGL engine test")

    #OpenGL setup
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

    #Custom setup, loading objects
    Load_map("./maps/test.map")
    CreateBufferForObjects()

    #Rendering loop, done once a frame
    while 1:

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #RENDER HERE
        for model in objects:
            Render(model)

        glRotatef(1,0,1,0)
        
        pygame.display.flip()
        #pygame.time.wait(1)


Main()
