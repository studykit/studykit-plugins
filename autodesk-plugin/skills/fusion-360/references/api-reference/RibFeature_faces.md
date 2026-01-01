# RibFeature.faces Property

Parent Object: [RibFeature](RibFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RibFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ribFeature\_var" is a variable referencing a RibFeature object.  ```` ``` # Get the value of the property. propertyValue = ribFeature_var.faces ``` ```` |

"ribFeature\_var" is a variable referencing a RibFeature object. ```` ``` #include <Fusion/Features/RibFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = ribFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |