# Viewport.camera Property

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Gets and sets the camera associated with the view. The camera returned is a copy of the current camera settings of the view. Editing the properties of the camera will have no affect on the viewport until the camera is assigned back to the viewport.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a Viewport object. |

"viewport\_var" is a variable referencing a Viewport object. ```` ``` #include <Core/Application/Viewport.h>  // Get the value of the property. Ptr<Camera> propertyValue = viewport_var->camera();  // Set the value of the property, where value_var is a Camera. bool returnValue = viewport_var->camera(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Camera](Camera.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [As-Built Joint Sample](AsBuiltJointSample_Sample.htm) | Demonstrates creating a new As-Built Joint. |
| [Joint Origin Sample](JointOriginSample_Sample.htm) | Demonstrates creating a new Joint Origin. |
| [Rendering Sample](RenderSample_Sample.htm) | Demonstrates using the Rendering capabilities in the API. This starts a series of local renderings to generate a series of frames, where the camera is repositioned and a parameter is modified for each frame to create a dynamic animation. To use the sample, have a design open that contains a parameter named "Length". It can be a user or model parameter. The sample will modify this parameter from a value of 0.1 cm to 15 cm, but you can change these values by editing the values of the paramStartVal and paramEndVal variables on lines 90 and 91 of the sample. It expects a folder named "C:\Temp\RenderSample" to exist, and will fail if it doesn't. The rendered frames will be written to that folder.  An example rendering is shown below where [this file](../ExtraFiles/RenderSample.f3d) was used. The parameter is modifying a move feature which results in changing the shape of an extrusion. The parameter could be driving anything and you could modify the code to edit more than one parameter. The result of this sample is a folder containing all of the rendered frames. You can process these to create an animation. The sample animation was created using GIMP.  ![Render Animation Sample](../images/RenderAnimationSample.gif) |
| [Rigid Group API Sample](RigidGroupSample_Sample.htm) | Demonstrates creating a new Rigid Group. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |