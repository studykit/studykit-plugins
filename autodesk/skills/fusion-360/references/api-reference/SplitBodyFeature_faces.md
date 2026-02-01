# SplitBodyFeature.faces Property

Parent Object: [SplitBodyFeature](SplitBodyFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeature\_var" is a variable referencing a SplitBodyFeature object.  ```` ``` # Get the value of the property. propertyValue = splitBodyFeature_var.faces ``` ```` |

"splitBodyFeature\_var" is a variable referencing a SplitBodyFeature object. ```` ``` #include <Fusion/Features/SplitBodyFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = splitBodyFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |