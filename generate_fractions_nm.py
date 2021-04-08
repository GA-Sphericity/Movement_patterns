from math import pi, sin, cos, sqrt
from random import shuffle
import turtle as t
import json

def sort_indices(n, m):
    indices = []
    add = 0
    while len(indices) < n:
        for i in range(m):
            index = (i*n)//m + int(bool( (i*n)%m )) + add
            if index < n and len(indices) < n and index not in indices:
                indices.append(index)
        add +=1

    return indices
        

def generate(n, m, scale_by_radius = False):

    angle_list = [pi/n * i  for i in range(n)]
    scale_factor = pi if scale_by_radius else 2*pi
    raw_movements = [[scale_factor*cos(u), scale_factor*sin(u)] for u in angle_list]
    del angle_list
   
    order = sort_indices(n, m)
    print(order)
    ordered_movements = [ raw_movements[i] for i in order ]
    
    def distance_points(point1, point2):
        ''' returns the distance between two points on the form [x,y] '''
        
        dist =  sqrt( (point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 )
        return dist
        
    def path_to_mid(old_point, movement, midpoint):
        ''' Finds wheter or not a vector should be multiplied by -1 (i.e roated 180 degrees),
            in order to move towards a given midpoint from a given position.
            returns the new position aswell as the vector with correct direction. '''
        
        newplus = [ old_point[0]+movement[0], old_point[1]+movement[1] ]
        newminus = [ old_point[0]-movement[0], old_point[1]-movement[1] ]
        if distance_points(newplus, midpoint) > distance_points(newminus, midpoint):
            return newminus, [ -movement[0], -movement[1] ]
        else:
            return newplus, movement

    midpoint = [scale_factor/2,0]
    position = [ [0, 0] ]
    movements = []

    for i in ordered_movements:
        pos, move = path_to_mid( position[-1], i, midpoint )
        position.append( pos )
        movements.append( move )
    
    t.clear()
    scale = 25
    t.speed(500)
    t.penup()
    t.setpos(position[0][0]*scale, position[0][1]*scale)
    t.pendown()
    t.speed(50)
    for p in position[1:]:
        t.setpos(p[0]*scale, p[1]*scale)

    return position, movements

def generate_json(n, m, output_path, scale_by_radius = False):
    position, movement = generate(n, m, scale_by_radius)
    result_dict = {
        "movement" : [ {"x" : m[0], "y" : m[1]} for m in movement ],
        "position" : [ {"x" : p[0], "y" : p[1]} for p in position ]
        }
    write = json.dumps(result_dict, indent=2)
    with open(output_path, "w") as tmp_file:
        tmp_file.write(write)

def gj(n, m, o): #shorneted version of generate_json for use in command line
    filename = rf"\n{n}_m{m}.json"
    generate_json(n, m, o+filename)

'''
path = input("output directory: ")
nm_raw = input("n,m: ")
nm_raw = nm_raw.split(",")
try:
    n = int(nm_raw[0])
    m = int(nm_raw[1])
except:
    print("retard")
    
gj(n, m, path)
input("ENTER to close")
'''

