# FaceGroup.entityToken Property![](../images/TestTubeLarge.png)

Parent Object: [FaceGroup](FaceGroup.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/FaceGroup.h>

## Description

Returns a token for the face group object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"faceGroup\_var" is a variable referencing a FaceGroup object.  ```` ``` # Get the value of the property. propertyValue = faceGroup_var.entityToken ``` ```` |

"faceGroup\_var" is a variable referencing a FaceGroup object. ```` ``` #include <Fusion/MeshBody/FaceGroup.h>  // Get the value of the property. string propertyValue = faceGroup_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |