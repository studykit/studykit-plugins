# ReplaceFaceFeature.targetFaces Property

Parent Object: [ReplaceFaceFeature](ReplaceFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeature.h>

## Description

Gets and sets the entities that define the target faces. The new faces must completely intersect the part. The collection can contain the surface faces, surface bodies and construction planes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeature\_var" is a variable referencing a ReplaceFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = replaceFaceFeature_var.targetFaces  # Set the value of the property. replaceFaceFeature_var.targetFaces = propertyValue ``` ```` |

"replaceFaceFeature\_var" is a variable referencing a ReplaceFaceFeature object. ```` ``` #include <Fusion/Features/ReplaceFaceFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = replaceFaceFeature_var->targetFaces();  // Set the value of the property, where value_var is a Base. bool returnValue = replaceFaceFeature_var->targetFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |