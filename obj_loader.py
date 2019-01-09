#import numpy as np
#from pyrr import Vector3

class Face:
    def __init__(self, vert, textc, norm):
        self.vertices = vert
        self.texture_cordinates = textc
        self.normals = norm
        

class Object:
    def __init__(self,vertices,faces,texture_cordinates,normals,name,path):
        self.vertices = vertices
        self.faces = faces
        self.texture_cordinates = texture_cordinates
        self.normals = normals
        
        self.name = name
        self.path = path

        #self.pos = pos
        #self.rot = rot
        #self.scale = scale

        
def load(path):
    vertices = []
    faces = []
    texture_cordinates = []
    normals = []
    name = "Unknown model"
    
    with open(path, "r") as f:
        for line in f:
            #Vertices
            if "v " in line:
                parts = line.split(" ")
                vertex = [float(parts[1]),float(parts[2]),float(parts[3])]
                vertices.append(vertex)
                

            #Faces
            if "f " in line:
                parts = line.split(" ")
                del(parts[0])

                _vertices = [int(parts[0].split("/")[0])-1, int(parts[1].split("/")[0])-1, int(parts[2].split("/")[0])-1]
                _texture_cordinates = [int(parts[0].split("/")[1])-1, int(parts[1].split("/")[1])-1, int(parts[2].split("/")[1])-1]
                _normals = [int(parts[0].split("/")[2])-1, int(parts[1].split("/")[2])-1, int(parts[2].split("/")[2])-1]
                faces.append(Face(_vertices,_texture_cordinates,_normals))
                

            #Texture cordinates
            if "vt " in line:
                parts = line.split(" ")
                cordinate = [float(parts[1]),float(parts[2])]
                texture_cordinates.append(cordinate)
                

            #Normals
            if "vn " in line:
                parts = line.split(" ")
                normal = [float(parts[1]),float(parts[2]),float(parts[3])]
                normals.append(normal)

            #Name
            if "o " in line:
                name = line[2:len(line)-1]

    return(Object(vertices, faces, texture_cordinates, normals,name,path))

#Test:          
#load("D:\\xd.obj")
