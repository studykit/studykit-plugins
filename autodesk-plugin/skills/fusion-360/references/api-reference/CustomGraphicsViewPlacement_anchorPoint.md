# CustomGraphicsViewPlacement.anchorPoint Property

Parent Object: [CustomGraphicsViewPlacement](CustomGraphicsViewPlacement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsViewPlacement.h>

## Description

Gets and sets the position within the defined graphics that serves as the anchor. This is the location on the graphics that is positioned at the specified view point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsViewPlacement\_var" is a variable referencing a CustomGraphicsViewPlacement object. |

"customGraphicsViewPlacement\_var" is a variable referencing a CustomGraphicsViewPlacement object. ```` ``` #include <Fusion/Graphics/CustomGraphicsViewPlacement.h>  // Get the value of the property. Ptr<Point3D> propertyValue = customGraphicsViewPlacement_var->anchorPoint();  // Set the value of the property, where value_var is a Point3D. bool returnValue = customGraphicsViewPlacement_var->anchorPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |