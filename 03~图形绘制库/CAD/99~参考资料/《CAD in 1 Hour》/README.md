> [原文地址](https://fab.cba.mit.edu/classes/865.24/topics/design-tools/)

# CAD in 1 Hour

### The Lay of the Land

Computer Aided Design (CAD) tools can be categorized in a variety of different ways. At a high-level you can separate tools based on how they represent geometry, such as whether objects are modeled by their exterior geometry or the interior space the object takes up. In other words is the object defined by its boundary or its volume. Is that geometric representation continuous or discrete (and limited to a particular resolution)?

Below we depict some CAD tools categorized by these dimensions (boundary/volume, continuous/discrete):

![img](https://fab.cba.mit.edu/classes/865.24/topics/design-tools/assets/cad-landscape.png)

Note that these categorizations are not formal and some tools may blur the lines between them or support multiple representations. For example standard **solid** modeling tools for mechanical engineer (such as SolidWorks or Fusion360) use boundary representations (B-Reps). These tools are designed to create solid models (as the name suggests) with watertight or manifold geometry. Some CAD tools restrict users to designing objects which are solid even though the underlying representation could describe non-solid geometry.

Another useful categorization of tools is parametric versus direct modeling (or non-parametric).

![img](https://fab.cba.mit.edu/classes/865.24/topics/design-tools/assets/parametric-vs-direct.png)

In direct modeling tools users specify geometry manually, whereas in parametric design tools geometry can by derived from other features or abstract operations.

Parameterization can take many forms. One of the most general and common ways of parameterizing systems is simply coding.

Of course programs can be used to represent practically anything, including 3D designs.

This is demonstrated below with a simple OpenSCAD design.

![img](https://fab.cba.mit.edu/classes/865.24/topics/design-tools/assets/openscad.png)

To designers using Rhino parameterization may come from plug-ins such as Grasshopper (check out [Nodi3D](https://nodi3d.com/) for something similar which is web-based and open source).

![img](https://fab.cba.mit.edu/classes/865.24/topics/design-tools/assets/grasshopper.png)

A similar dataflow programming environment could be familiar to an artist using Blender's geometry nodes.

![img](https://fab.cba.mit.edu/classes/865.24/topics/design-tools/assets/blender-nodes.png)

To mechanical engineers parameterization generally comes from geometric constraint solvers and timelines of operations. We'll have a lot to say about constraint solvers later in this write-up.

![img](https://fab.cba.mit.edu/classes/865.24/topics/design-tools/assets/onshape.png)

We're going to introduce you to some of the key concepts needed to create design tools. We will introduce many of these concepts by demonstrating how to implement minimal versions of them in code (JavaScript!). We will cover how to represent solids with distance fields, how to mesh those fields, some history of modern solid modeling CAD tools, constraint solvers, B-Reps through the context of the step format, and survey a few futuristic generative design tools.

Let's get into it.
