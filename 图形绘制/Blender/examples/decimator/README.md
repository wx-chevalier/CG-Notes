# BlenderPythonDecimator

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3476899.svg)](https://doi.org/10.5281/zenodo.3476899) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/HusseinBakri/BlenderPythonDecimator) ![GitHub](https://img.shields.io/github/license/HusseinBakri/BlenderPythonDecimator)

A Python Tool that decimates a .obj 3D model into a lower resolutions using the Blender Python API.

# Description

A Blender (https://www.blender.org/) Python 3 tool to simplify or decimate a 3D Model/Mesh (With and Without Textures) in OBJ format into a lower resolution mesh taking a specific ratio that governs the Number of Faces. It uses Blender Python API (https://docs.blender.org/api/2.79/). Download path: https://download.blender.org/release/Blender2.79/

The Python tool takes CLI arguments such as the ratio, the original mesh and the name of final decimated mesh.

You can change my code, in a very simple manner, to import and export other types of 3D file formats supported by Blender in the following manner:

```
# Pay ATTENTION to extentions of files: Collada (.dae), FBX (.fbx), X3D (.x3d), Wavefront OBJ (.obj) etc...
# For OJB Format
# Importing a model in Wavefront OBJ (used in my Tool)
bpy.ops.import_scene.obj(filepath=input_model)

# Exporting a model in Wavefront OBJ (used in my Tool)
bpy.ops.export_scene.obj(filepath=output_model)

# For Collada Format
# Importing .collada
bpy.ops.wm.collada_import(filepath=input_model)

# Exporting .collada
bpy.ops.wm.collada_export(filepath=output_model)

# For Extensible 3D (.x3d)
# Importing X3D Format
bpy.ops.import_scene.x3d(filepath=input_model)

# Exporting X3D Format
bpy.ops.export_scene.x3d(filepath=output_model)

# For FBX (.fbx)
# Importing FBX
bpy.ops.import_scene.fbx(filepath=input_model)

# Exporting FBX
bpy.ops.export_scene.fbx(filepath=output_model)
```

# Requirements

Installing Blender on the Operating System (OS) in question.

Example in Ubuntu Server 16.04: 'sudo apt-get install blender'

Example in Fedora 26: 'sudo dnf install blender'

NB: Make sure also you can call Blender from the command line or terminal of your OS.

## Mac OS

In Mac OS, Blender may be an unrecognized command so you need to create an alias so it can be used from terminal
Normally the Blender command or process is inside the blender.app folder. Do the following:

```
echo 'alias blender="/Applications/blender.app/Contents/MacOS/blender"' >> .bashrc
```

or normally you can also find it in a folder in /Applications called also Blender

```
echo 'alias blender="/Applications/Blender/blender.app/Contents/MacOS/blender"' >> .bashrc

```

Now run this in the terminal:

```
source ~/.bashrc
```

Finally check if Blender can be invoked from the terminal:

```
blender --version
```

# Usage

```
blender -b -P blenderSimplify.py -- --ratio X --inm 'Original_Mesh.obj' --outm 'Output_Mesh.obj'

After --inm:  you specify the original mesh to import for decimation
      --outm: you specify the final output mesh name to export
      --ratio: this ratio should be between 0.1 and 1.0(no decimation occurs). If you choose per example --ratio 0.5 meaning you half the number of faces so if your model is 300K faces it will be exported as 150K faces

PS: this tool does not try to preserve the integrity of the mesh so be carefull in choosing the ratio (try not choose a very low ratio)

##Another enhanced version which stores the output 3D model and its textures in a folder named as the ratio of decimation

blender -b -P blenderSimplifyV2.py -- --ratio 0.5 --inm 'Original_Mesh.obj' --outm 'Output_Mesh.obj'

##A third version of the tool which takes as a parameter the number of faces instead of a ratio of decimation
(which can be very handy if you know that you want an exact number of faces for the output 3D Model)

blender -b -P blenderSimplifyNumFaces.py -- --nfaces 300000 --inm 'Original_Mesh.obj' --outm 'Output_Mesh.obj'

```

# Examples

blender -b -P blenderSimplify.py -- --ratio 0.5 --inm 'Hat.obj' --outm 'Hat_simple.obj'

blender -b -P blenderSimplifyV2.py -- --ratio 0.5 --inm 'Hat.obj' --outm 'Hat_simple.obj'

blender -b -P blenderSimplifyNumFaces.py -- --nfaces 300000 --inm 'Hat.obj' --outm 'Hat_simple.obj'

# Other similar tools that I developped

Have a look at a Meshlab Python Decimator that I created at https://github.com/HusseinBakri/3DMeshBulkSimplification.

# License

This program is licensed under GNU GPL v3 License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution of this work. The attribution should include the title of the program, the author and the site or the document where the program is taken from.
