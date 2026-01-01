# ExtendFeature.faces Property

Parent Object: [ExtendFeature](ExtendFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeature\_var" is a variable referencing an ExtendFeature object.  ```` ``` # Get the value of the property. propertyValue = extendFeature_var.faces ``` ```` |

"extendFeature\_var" is a variable referencing an ExtendFeature object. ```` ``` #include <Fusion/Features/ExtendFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = extendFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |