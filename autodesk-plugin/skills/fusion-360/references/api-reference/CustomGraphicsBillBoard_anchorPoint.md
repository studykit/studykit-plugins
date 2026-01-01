# CustomGraphicsBillBoard.anchorPoint Property

Parent Object: [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBillBoard.h>

## Description

RETIRED - This property has been retired. It is not needed since the matrix defined for the CustomGraphicsText object defines the position and anchor for the billboarded text. Getting the value of this property will return a point at the origin. Setting this property will be ignored.
Specifies the coordinate in model or view space that the graphics will anchor to. For graphics that represent a label, this will typically be the point where the label attaches to the model. A CustomGraphicsAnchorPoint can be created using the static create method on the CustomGraphicsAnchorPoint object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBillBoard\_var" is a variable referencing a CustomGraphicsBillBoard object. |

"customGraphicsBillBoard\_var" is a variable referencing a CustomGraphicsBillBoard object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBillBoard.h>  // Get the value of the property. Ptr<Point3D> propertyValue = customGraphicsBillBoard_var->anchorPoint();  // Set the value of the property, where value_var is a Point3D. bool returnValue = customGraphicsBillBoard_var->anchorPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |