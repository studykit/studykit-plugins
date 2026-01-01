# CombineFeature.faces Property

Parent Object: [CombineFeature](CombineFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeature\_var" is a variable referencing a CombineFeature object.  ```` ``` # Get the value of the property. propertyValue = combineFeature_var.faces ``` ```` |

"combineFeature\_var" is a variable referencing a CombineFeature object. ```` ``` #include <Fusion/Features/CombineFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = combineFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |