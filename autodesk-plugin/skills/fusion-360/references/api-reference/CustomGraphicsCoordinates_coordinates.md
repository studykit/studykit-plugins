# CustomGraphicsCoordinates.coordinates Property

Parent Object: [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCoordinates.h>

## Description

Gets and sets the coordinate data associated with this CustomGraphicsCoordinates object. This data represents the x, y, z components of the coordinates where the unit of measure is centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCoordinates\_var" is a variable referencing a CustomGraphicsCoordinates object. |

"customGraphicsCoordinates\_var" is a variable referencing a CustomGraphicsCoordinates object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCoordinates.h>  // Get the value of the property. std::vector<double> propertyValue = customGraphicsCoordinates_var->coordinates();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsCoordinates_var->coordinates(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type double.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |