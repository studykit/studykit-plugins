# FlatPattern.sideFaces Property

Parent Object: [FlatPattern](FlatPattern.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPattern.h>

## Description

Returns the "side" faces of the flat pattern B-Rep body. These are the faces around the edge of the flat pattern that connect the top and bottom faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPattern\_var" is a variable referencing a FlatPattern object. |

"flatPattern\_var" is a variable referencing a FlatPattern object. ```` ``` #include <Fusion/SheetMetal/FlatPattern.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = flatPattern_var->sideFaces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |