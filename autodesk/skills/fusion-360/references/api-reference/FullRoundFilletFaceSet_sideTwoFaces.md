# FullRoundFilletFaceSet.sideTwoFaces Property

Parent Object: [FullRoundFilletFaceSet](FullRoundFilletFaceSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FullRoundFilletFaceSet.h>

## Description

Gets the side two faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fullRoundFilletFaceSet\_var" is a variable referencing a FullRoundFilletFaceSet object.  ```` ``` # Get the value of the property. propertyValue = fullRoundFilletFaceSet_var.sideTwoFaces ``` ```` |

"fullRoundFilletFaceSet\_var" is a variable referencing a FullRoundFilletFaceSet object. ```` ``` #include <Fusion/Features/FullRoundFilletFaceSet.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = fullRoundFilletFaceSet_var->sideTwoFaces(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |