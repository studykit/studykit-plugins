# FullRoundFilletFaceSet.centerFace Property

Parent Object: [FullRoundFilletFaceSet](FullRoundFilletFaceSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FullRoundFilletFaceSet.h>

## Description

Gets the center face associated with this full round fillet face set. When a center face has tangentially connected faces then all the tangentially connected faces will be filleted automatically.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fullRoundFilletFaceSet\_var" is a variable referencing a FullRoundFilletFaceSet object.  ```` ``` # Get the value of the property. propertyValue = fullRoundFilletFaceSet_var.centerFace ``` ```` |

"fullRoundFilletFaceSet\_var" is a variable referencing a FullRoundFilletFaceSet object. ```` ``` #include <Fusion/Features/FullRoundFilletFaceSet.h>  // Get the value of the property. Ptr<BRepFace> propertyValue = fullRoundFilletFaceSet_var->centerFace(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFace](BRepFace.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |