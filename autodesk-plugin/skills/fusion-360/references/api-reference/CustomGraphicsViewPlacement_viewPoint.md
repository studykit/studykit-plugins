# CustomGraphicsViewPlacement.viewPoint Property

Parent Object: [CustomGraphicsViewPlacement](CustomGraphicsViewPlacement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsViewPlacement.h>

## Description

A 2D point in the view that defines the position of the graphics. This is relative to the corner and is in pixels. The x and y directions vary for each of the corners. These directions are only used to position the 2D point and do not affect the standard coordinate system the graphics were drawn in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsViewPlacement\_var" is a variable referencing a CustomGraphicsViewPlacement object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsViewPlacement_var.viewPoint  # Set the value of the property. customGraphicsViewPlacement_var.viewPoint = propertyValue ``` ```` |

"customGraphicsViewPlacement\_var" is a variable referencing a CustomGraphicsViewPlacement object. ```` ``` #include <Fusion/Graphics/CustomGraphicsViewPlacement.h>  // Get the value of the property. Ptr<Point2D> propertyValue = customGraphicsViewPlacement_var->viewPoint();  // Set the value of the property, where value_var is a Point2D. bool returnValue = customGraphicsViewPlacement_var->viewPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point2D](Point2D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |