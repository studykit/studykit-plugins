# Rendering.resolution Property

Parent Object: [Rendering](Rendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/Rendering.h>

## Description

Gets and sets the resolution of the rendered image. This is the final width and height of the image in pixels. To define a custom aspect ratio, use the resolutionHeight and resolutionWidth properties to define any resolution. Using those has the side effect of setting this property to CustomRenderResolution. Setting this to anything except CustomRenderResolution, will also have the side effect of setting the aspect ratio.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rendering\_var" is a variable referencing a Rendering object. |

"rendering\_var" is a variable referencing a Rendering object. ```` ``` #include <Fusion/Render/Rendering.h>  // Get the value of the property. RenderResolutions propertyValue = rendering_var->resolution();  // Set the value of the property, where value_var is a RenderResolutions. bool returnValue = rendering_var->resolution(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [RenderResolutions](RenderResolutions.htm).

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