# CustomGraphicsViewScale.anchorPoint Property

Parent Object: [CustomGraphicsViewScale](CustomGraphicsViewScale.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsViewScale.h>

## Description

Gets and sets the point in the graphics that defines the origin of the scaling. The graphics will be scaled up or down relative to that point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsViewScale\_var" is a variable referencing a CustomGraphicsViewScale object. |

"customGraphicsViewScale\_var" is a variable referencing a CustomGraphicsViewScale object. ```` ``` #include <Fusion/Graphics/CustomGraphicsViewScale.h>  // Get the value of the property. Ptr<Point3D> propertyValue = customGraphicsViewScale_var->anchorPoint();  // Set the value of the property, where value_var is a Point3D. bool returnValue = customGraphicsViewScale_var->anchorPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |