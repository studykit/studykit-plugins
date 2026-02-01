# CustomGraphicsLines.coordinates Property

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

Gets and sets the CustomGraphicsCoordinates object that defines the coordinates of the vertices of the lines. A CustomGraphicsCoordinates object can be created using the static create method of the CustomGraphicsCoordinates class.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. |

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. ```` ``` #include <Fusion/Graphics/CustomGraphicsLines.h>  // Get the value of the property. Ptr<CustomGraphicsCoordinates> propertyValue = customGraphicsLines_var->coordinates();  // Set the value of the property, where value_var is a CustomGraphicsCoordinates. bool returnValue = customGraphicsLines_var->coordinates(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |