# CustomGraphicsLines.lineStripLengths Property

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

If isLineStrip is true, this property defines the number of coordinates to use in the line strips. It is an array of integers that defines the number of coordinates for each line strip. An empty array indicates that a single line strip is to be drawn.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. |

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. ```` ``` #include <Fusion/Graphics/CustomGraphicsLines.h>  // Get the value of the property. std::vector<integer> propertyValue = customGraphicsLines_var->lineStripLengths();  // Set the value of the property, where value_var is an integer. bool returnValue = customGraphicsLines_var->lineStripLengths(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type integer.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |