# MeshRemeshFeatures.createInput Method![](../images/TestTubeLarge.png)

Parent Object: [MeshRemeshFeatures](MeshRemeshFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshRemeshFeatures.h>

## Description

Creates a MeshRemeshFeatureInput object. Use properties and methods on this object to define the mesh re-mesh you want to create and then use the add method, passing in the MeshRemeshFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshRemeshFeatures\_var" is a variable referencing a [MeshRemeshFeatures](MeshRemeshFeatures.htm) object.```` ``` returnValue = meshRemeshFeatures_var.createInput(mesh) ``` ```` |

"meshRemeshFeatures\_var" is a variable referencing a [MeshRemeshFeatures](MeshRemeshFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshRemeshFeatureInput](MeshRemeshFeatureInput.htm) | Returns the newly created MeshRemeshFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| mesh | [Base](Base.htm) | A MeshBody in either a parametric or direct modeling design. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |