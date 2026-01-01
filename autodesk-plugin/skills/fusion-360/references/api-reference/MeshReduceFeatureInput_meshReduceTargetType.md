# MeshReduceFeatureInput.meshReduceTargetType Property![](../images/TestTubeLarge.png)

Parent Object: [MeshReduceFeatureInput](MeshReduceFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshReduceFeatureInput.h>

## Description

Gets and sets the target criteria for the reduction, default value is MaximumDeviationMeshReduceTargetType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshReduceFeatureInput\_var" is a variable referencing a MeshReduceFeatureInput object. |

"meshReduceFeatureInput\_var" is a variable referencing a MeshReduceFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshReduceFeatureInput.h>  // Get the value of the property. MeshReduceTargetTypes propertyValue = meshReduceFeatureInput_var->meshReduceTargetType();  // Set the value of the property, where value_var is a MeshReduceTargetTypes. bool returnValue = meshReduceFeatureInput_var->meshReduceTargetType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MeshReduceTargetTypes](MeshReduceTargetTypes.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |