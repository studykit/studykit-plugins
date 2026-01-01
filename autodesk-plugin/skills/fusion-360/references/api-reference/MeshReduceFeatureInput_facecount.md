# MeshReduceFeatureInput.facecount Property![](../images/TestTubeLarge.png)

Parent Object: [MeshReduceFeatureInput](MeshReduceFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshReduceFeatureInput.h>

## Description

Gets and sets the target face count for the reduced mesh as a target for the reduction. Only valid if meshReduceTargetType is FaceCountMeshReduceTargetType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshReduceFeatureInput\_var" is a variable referencing a MeshReduceFeatureInput object. |

"meshReduceFeatureInput\_var" is a variable referencing a MeshReduceFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshReduceFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = meshReduceFeatureInput_var->facecount();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = meshReduceFeatureInput_var->facecount(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |