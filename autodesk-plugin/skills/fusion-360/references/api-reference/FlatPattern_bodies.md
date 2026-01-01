# FlatPattern.bodies Property

Parent Object: [FlatPattern](FlatPattern.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPattern.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPattern\_var" is a variable referencing a FlatPattern object.  ```` ``` # Get the value of the property. propertyValue = flatPattern_var.bodies ``` ```` |

"flatPattern\_var" is a variable referencing a FlatPattern object. ```` ``` #include <Fusion/SheetMetal/FlatPattern.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = flatPattern_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |