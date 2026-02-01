# RevolveFeature.endFaces Property

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Property that returns the set of faces that cap the end of the revolve opposite the start faces. In the case where there aren't any start faces, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a RevolveFeature object. |

"revolveFeature\_var" is a variable referencing a RevolveFeature object. ```` ``` #include <Fusion/Features/RevolveFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = revolveFeature_var->endFaces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |