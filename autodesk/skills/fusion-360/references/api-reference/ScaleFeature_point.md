# ScaleFeature.point Property

Parent Object: [ScaleFeature](ScaleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeature.h>

## Description

Gets and sets the point as reference to scale. This can be a BRepVertex, a SketchPoint or a ConstructionPoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeature\_var" is a variable referencing a ScaleFeature object.  ```` ``` # Get the value of the property. propertyValue = scaleFeature_var.point  # Set the value of the property. scaleFeature_var.point = propertyValue ``` ```` |

"scaleFeature\_var" is a variable referencing a ScaleFeature object. ```` ``` #include <Fusion/Features/ScaleFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = scaleFeature_var->point();  // Set the value of the property, where value_var is a Base. bool returnValue = scaleFeature_var->point(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |