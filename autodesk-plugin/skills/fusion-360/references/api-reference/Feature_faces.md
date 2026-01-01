# Feature.faces Property

Parent Object: [Feature](Feature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Feature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"feature\_var" is a variable referencing a Feature object.  ```` ``` # Get the value of the property. propertyValue = feature_var.faces ``` ```` |

"feature\_var" is a variable referencing a Feature object. ```` ``` #include <Fusion/Features/Feature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = feature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |