# MoveFeature.faces Property

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a MoveFeature object.  ```` ``` # Get the value of the property. propertyValue = moveFeature_var.faces ``` ```` |

"moveFeature\_var" is a variable referencing a MoveFeature object. ```` ``` #include <Fusion/Features/MoveFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = moveFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |