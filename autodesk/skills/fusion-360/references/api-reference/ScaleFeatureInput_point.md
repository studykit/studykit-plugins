# ScaleFeatureInput.point Property

Parent Object: [ScaleFeatureInput](ScaleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatureInput.h>

## Description

Gets and sets the origin point of the scale. This can be a BRepVertex, a SketchPoint or a ConstructionPoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object. |

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object. ```` ``` #include <Fusion/Features/ScaleFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = scaleFeatureInput_var->point();  // Set the value of the property, where value_var is a Base. bool returnValue = scaleFeatureInput_var->point(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |