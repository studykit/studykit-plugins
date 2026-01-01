# HoleFeature.sideFaces Property

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Property that returns all of the side faces of the hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a HoleFeature object. |

"holeFeature\_var" is a variable referencing a HoleFeature object. ```` ``` #include <Fusion/Features/HoleFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = holeFeature_var->sideFaces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |