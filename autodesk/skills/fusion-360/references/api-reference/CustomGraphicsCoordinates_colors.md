# CustomGraphicsCoordinates.colors Property

Parent Object: [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCoordinates.h>

## Description

Gets and sets the colors associated with the coordinate data. This is used when a mesh is displayed using per-vertex coloring. The color at each vertex is represented by four values where they are the red, green, blue, and alpha values. This should contain the same number of colors as vertices.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCoordinates\_var" is a variable referencing a CustomGraphicsCoordinates object. |

"customGraphicsCoordinates\_var" is a variable referencing a CustomGraphicsCoordinates object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCoordinates.h>  // Get the value of the property. std::vector<short> propertyValue = customGraphicsCoordinates_var->colors();  // Set the value of the property, where value_var is a short. bool returnValue = customGraphicsCoordinates_var->colors(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type short.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |