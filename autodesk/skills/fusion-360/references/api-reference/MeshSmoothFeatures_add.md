# MeshSmoothFeatures.add Method![](../images/TestTubeLarge.png)

Parent Object: [MeshSmoothFeatures](MeshSmoothFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshSmoothFeatures.h>

## Description

Creates a mesh smooth feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshSmoothFeatures\_var" is a variable referencing a [MeshSmoothFeatures](MeshSmoothFeatures.htm) object.```` ``` returnValue = meshSmoothFeatures_var.add(input) ``` ```` |

"meshSmoothFeatures\_var" is a variable referencing a [MeshSmoothFeatures](MeshSmoothFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshSmoothFeature](MeshSmoothFeature.htm) | Returns the newly created MeshSmoothFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MeshSmoothFeatureInput](MeshSmoothFeatureInput.htm) | A MeshSmoothFeatureInput object that defines the desired MeshSmooth feature. Use the createInput method to create a new MeshSmoothFeatureInput object and then use methods on it (the MeshSmoothFeatureInput object) to define the smoothing. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |