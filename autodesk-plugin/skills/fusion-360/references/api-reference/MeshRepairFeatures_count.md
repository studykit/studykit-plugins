# MeshRepairFeatures.count Property![](../images/TestTubeLarge.png)

Parent Object: [MeshRepairFeatures](MeshRepairFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshRepairFeatures.h>

## Description

The number of mesh repair features in the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshRepairFeatures\_var" is a variable referencing a MeshRepairFeatures object. |

"meshRepairFeatures\_var" is a variable referencing a MeshRepairFeatures object. ```` ``` #include <Fusion/MeshBody/MeshRepairFeatures.h>  // Get the value of the property. uinteger propertyValue = meshRepairFeatures_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |