# ReverseNormalFeature.faces Property

Parent Object: [ReverseNormalFeature](ReverseNormalFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object.  ```` ``` # Get the value of the property. propertyValue = reverseNormalFeature_var.faces ``` ```` |

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object. ```` ``` #include <Fusion/Features/ReverseNormalFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = reverseNormalFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |