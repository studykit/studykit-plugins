# UnstitchFeature.faces Property

Parent Object: [UnstitchFeature](UnstitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object.  ```` ``` # Get the value of the property. propertyValue = unstitchFeature_var.faces ``` ```` |

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object. ```` ``` #include <Fusion/Features/UnstitchFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = unstitchFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |