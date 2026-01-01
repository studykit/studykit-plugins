# MeshRepairFeature.meshRepairRebuildType Property![](../images/TestTubeLarge.png)

Parent Object: [MeshRepairFeature](MeshRepairFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshRepairFeature.h>

## Description

Gets and sets the type of mesh repair rebuild mode. Only valid if meshRepairType is RebuildMeshRepairType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshRepairFeature\_var" is a variable referencing a MeshRepairFeature object. |

"meshRepairFeature\_var" is a variable referencing a MeshRepairFeature object. ```` ``` #include <Fusion/MeshBody/MeshRepairFeature.h>  // Get the value of the property. MeshRepairRebuildTypes propertyValue = meshRepairFeature_var->meshRepairRebuildType();  // Set the value of the property, where value_var is a MeshRepairRebuildTypes. bool returnValue = meshRepairFeature_var->meshRepairRebuildType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MeshRepairRebuildTypes](MeshRepairRebuildTypes.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |