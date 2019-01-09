#MODERN OPENGL SUPPORT


#class Face:
    #def __init__(self, vert, textc, norm):
        #self.vertices = vert
        #self.texture_cordinates = textc
        #self.normals = norm

    #vertices = []
    #texture_cordinates = []
    #normals = []
        

class Object:
    def __init__(self,vertices,order,order_textures,order_normals,texture_cordinates,normals,name,path):

        self.order = order
        self.order_textures = order_textures
        self.order_normals = order_normals

        self.vertices = vertices
        self.texture_cordinates = texture_cordinates
        self.normals = normals
        
        self.name = name
        self.path = path

        
def load(path):
    vertices = []
    order = []
    order_textures = []
    order_normals = []
    texture_cordinates = []
    normals = []
    name = "Unknown model"
    
    with open(path, "r") as f:
        for line in f:
            #Vertices
            if "v " in line:
                parts = line.split(" ")
                
                #vertex = [float(parts[1]),float(parts[2]),float(parts[3])]
                
                vertices.append(float(parts[1]))
                vertices.append(float(parts[2]))
                vertices.append(float(parts[3]))
                

            #Faces
            if "f " in line:
                parts = line.split(" ")
                del(parts[0])

                #_vertices = [int(parts[0].split("/")[0])-1, int(parts[1].split("/")[0])-1, int(parts[2].split("/")[0])-1]
                #_texture_cordinates = [int(parts[0].split("/")[1])-1, int(parts[1].split("/")[1])-1, int(parts[2].split("/")[1])-1]
                #_normals = [int(parts[0].split("/")[2])-1, int(parts[1].split("/")[2])-1, int(parts[2].split("/")[2])-1]
                #faces.append(Face(_vertices,_texture_cordinates,_normals))

                order.append(int(parts[0].split("/")[0])-1)
                order.append(int(parts[1].split("/")[0])-1)
                order.append(int(parts[2].split("/")[0])-1)

                order_textures.append(int(parts[0].split("/")[1])-1)
                order_textures.append(int(parts[1].split("/")[1])-1)
                order_textures.append(int(parts[2].split("/")[1])-1)
                
                order_normals.append(int(parts[0].split("/")[2])-1)
                order_normals.append(int(parts[1].split("/")[2])-1)
                order_normals.append(int(parts[2].split("/")[2])-1)

                

            #Texture cordinates
            if "vt " in line:
                parts = line.split(" ")
                
                #cordinate = [float(parts[1]),float(parts[2])]
                #texture_cordinates.append(cordinate)
                
                texture_cordinates.append(float(parts[1]))
                texture_cordinates.append(float(parts[2]))
                

            #Normals
            if "vn " in line:
                parts = line.split(" ")
                
                #normal = [float(parts[1]),float(parts[2]),float(parts[3])]
                #normals.append(normal)

                normals.append(float(parts[1]))
                normals.append(float(parts[2]))
                normals.append(float(parts[3]))

            #Name
            if "o " in line:
                name = line[2:len(line)-1]

    return(Object(vertices,order,order_textures,order_normals,texture_cordinates,normals,name,path))

#Test:          
obj = load("D:\\xd.obj")
print(obj.order_textures)
