# BoxFeature.faces Property

Parent Object: [BoxFeature](BoxFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeature\_var" is a variable referencing a BoxFeature object.  ```` ``` # Get the value of the property. propertyValue = boxFeature_var.faces ``` ```` |

"boxFeature\_var" is a variable referencing a BoxFeature object. ```` ``` #include <Fusion/Features/BoxFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = boxFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |