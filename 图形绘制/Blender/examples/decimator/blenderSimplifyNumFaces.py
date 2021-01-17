#!/usr/bin/python3
import bpy
import sys
import time
import argparse
import os
import platform
import shutil

'''
Description: This version of blenderSimplify.py takes this time the number of faces instead of the ratio
of decimation. This is more handy for batch decimation of 3D Models where you specify the number of faces. 
Requirements: You need only to install Blender first on the OS in question
          Example in Ubuntu Server 16.04: 'sudo apt-get install blender'
          Example in Fedora 26:           'sudo dnf install blender'
          Make sure you can call Blender from cmd/terminal etc...
Usage: blender -b -P blenderSimplifyNumFaces.py -- --nfaces 300000 --inm 'Original_Mesh.obj' --outm 'Output_Mesh.obj'
After --inm:  you specify the original mesh to import for decimation
      --outm: you specify the final output mesh name to export
      --ratio: this ratio should be between 0.1 and 1.0(no decimation occurs). If you choose
      Per example --ratio 0.5 meaning you half the number of faces so if your model is 300K faces
      it will be exported as 150K faces
PS: this tool does not try to preserve the integrity of the mesh so be carefull in choosing
the ratio (try not choose a very low ratio)
Enjoy!
'''
 
def get_args():
  parser = argparse.ArgumentParser()
 
  # get all script args
  _, all_arguments = parser.parse_known_args()
  double_dash_index = all_arguments.index('--')
  script_args = all_arguments[double_dash_index + 1: ]
 
  # add parser rules
  parser.add_argument('-nf', '--nfaces', help="Specify the exact number of faces")
  parser.add_argument('-in', '--inm', help="Original Model")
  parser.add_argument('-out', '--outm', help="Decimated output file")
  parsed_script_args, _ = parser.parse_known_args(script_args)
  return parsed_script_args
 
args = get_args()
Num_Of_Faces = int(args.nfaces)

input_model = str(args.inm)
print(input_model)

output_model = str(args.outm)
print(output_model)

print('\n Clearing blender scene (default garbage...)')
# deselect all
bpy.ops.object.select_all(action='DESELECT')

# selection
bpy.data.objects['Camera'].select = True

# remove it
bpy.ops.object.delete() 

# Clear Blender scene
# select objects by type
for o in bpy.data.objects:
    if o.type == 'MESH':
        o.select = True
    else:
        o.select = False

# call the operator once
bpy.ops.object.delete()

print('\nImporting the input 3D model, please wait.......')
bpy.ops.import_scene.obj(filepath=input_model)
print('\nObj file imported successfully ...')


#calculating the ratio of decimation from the number of faces
#################
objectList0=bpy.data.objects
meshes0 = []
vertices = 0
edges = 0
faces = 0

for obj in objectList0:
  if(obj.type == "MESH"):
    meshes0.append(obj)
    vertices = obj.data.vertices
    edges = obj.data.edges
    faces = obj.data.polygons

#print(len(vertices))
#print(len(edges))
#print(len(faces))

OriginalMeshNumFaces = float(len(faces))
print('\nOriginal Mesh number of faces.......')
print(OriginalMeshNumFaces)

#decimateRatio = Num_Of_Faces / Original Num_Of_Faces of the Mesh
decimateRatio = Num_Of_Faces / OriginalMeshNumFaces
print('\nRatio of decimation will be.......')
print(decimateRatio)

#Creating a folder named as the Number of faces: named '150000'
print('\n Creating a folder to store the decimated model ...........')
nameOfFolder = Num_Of_Faces
if not os.path.exists(str(nameOfFolder)):
    os.makedirs(str(nameOfFolder))


print('\n Beginning the process of Decimation using Blender Python API ...')
modifierName='DecimateMod'

print('\n Creating and object list and adding meshes to it ...')
objectList=bpy.data.objects
meshes = []
for obj in objectList:
  if(obj.type == "MESH"):
    meshes.append(obj)

print("{} meshes".format(len(meshes)))

for i, obj in enumerate(meshes):
  bpy.context.scene.objects.active = obj
  print("{}/{} meshes, name: {}".format(i, len(meshes), obj.name))
  print("{} has {} verts, {} edges, {} polys".format(obj.name, len(obj.data.vertices), len(obj.data.edges), len(obj.data.polygons)))
  modifier = obj.modifiers.new(modifierName,'DECIMATE')
  modifier.ratio = decimateRatio
  modifier.use_collapse_triangulate = True
  bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifierName)
  print("{} has {} verts, {} edges, {} polys after decimation".format(obj.name, len(obj.data.vertices), len(obj.data.edges), len(obj.data.polygons)))

bpy.ops.export_scene.obj(filepath=str(nameOfFolder) + "/" + output_model)
print('\nProcess of Decimation Finished ...')
print('\nOutput Mesh is stored in corresponding folder ...')

print('\n Copying textures (PNG and JPEG) into the folder of decimated model....')
#Now checking for textures in the folder of the input mesh.... (plz change if needed)
allfilelist= os.listdir('.')

for Afile in allfilelist[:]: 
    if not(Afile.endswith(".png") or Afile.endswith(".PNG") or Afile.endswith(".jpg") or Afile.endswith(".JPG")):
        allfilelist.remove(Afile)
print('\n Found the LIST of images in PNG and JPEG (textures): ')
print(allfilelist)

for file in allfilelist:
    shutil.copy(file, str(nameOfFolder))
