# CustomGraphicsLines.indexList Property

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

Gets and sets an array of integers that represent indices into the coordinates to define the order the coordinates are used to draw the lines. An empty array indicates that no index list is used and coordinates are used in the order they're provided in the provided CustomGraphicsCoordinates object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. |

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. ```` ``` #include <Fusion/Graphics/CustomGraphicsLines.h>  // Get the value of the property. std::vector<integer> propertyValue = customGraphicsLines_var->indexList();  // Set the value of the property, where value_var is an integer. bool returnValue = customGraphicsLines_var->indexList(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type integer.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |