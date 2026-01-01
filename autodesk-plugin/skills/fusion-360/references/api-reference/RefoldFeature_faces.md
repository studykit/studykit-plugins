# RefoldFeature.faces Property

Parent Object: [RefoldFeature](RefoldFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RefoldFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"refoldFeature\_var" is a variable referencing a RefoldFeature object.  ```` ``` # Get the value of the property. propertyValue = refoldFeature_var.faces ``` ```` |

"refoldFeature\_var" is a variable referencing a RefoldFeature object. ```` ``` #include <Fusion/SheetMetal/RefoldFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = refoldFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |