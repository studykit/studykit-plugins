# RenderManager.rendering Property

Parent Object: [RenderManager](RenderManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderManager.h>

## Description

Provides access to the local and cloud rendering capabilities of Fusion. In both cases, the rendering is done in a process external to Fusion, either a local or cloud rendering process.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderManager\_var" is a variable referencing a RenderManager object. |

"renderManager\_var" is a variable referencing a RenderManager object. ```` ``` #include <Fusion/Render/RenderManager.h>  // Get the value of the property. Ptr<Rendering> propertyValue = renderManager_var->rendering(); ``` ```` |

## Property Value

This is a read only property whose value is a [Rendering](Rendering.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Rendering Sample](RenderSample_Sample.htm) | Demonstrates using the Rendering capabilities in the API. This starts a series of local renderings to generate a series of frames, where the camera is repositioned and a parameter is modified for each frame to create a dynamic animation. To use the sample, have a design open that contains a parameter named "Length". It can be a user or model parameter. The sample will modify this parameter from a value of 0.1 cm to 15 cm, but you can change these values by editing the values of the paramStartVal and paramEndVal variables on lines 90 and 91 of the sample. It expects a folder named "C:\Temp\RenderSample" to exist, and will fail if it doesn't. The rendered frames will be written to that folder.  An example rendering is shown below where [this file](../ExtraFiles/RenderSample.f3d) was used. The parameter is modifying a move feature which results in changing the shape of an extrusion. The parameter could be driving anything and you could modify the code to edit more than one parameter. The result of this sample is a folder containing all of the rendered frames. You can process these to create an animation. The sample animation was created using GIMP.  ![Render Animation Sample](../images/RenderAnimationSample.gif) |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |