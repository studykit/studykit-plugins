# CustomGraphicsLines.isLineStrip Property

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

Defines if the coordinates are used to define a series of individual lines or a connected set of lines (line strip). If individual lines are drawn (this property is false), each pair of coordinates define a single line. If a line strip is drawn (this property is true), the first pair of coordinates define the first line and the third coordinate defines a line that connects to the second coordinate. The fourth coordinate creates a line connecting to the third coordinate, and so on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. |

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. ```` ``` #include <Fusion/Graphics/CustomGraphicsLines.h>  // Get the value of the property. boolean propertyValue = customGraphicsLines_var->isLineStrip();  // Set the value of the property, where value_var is a boolean. bool returnValue = customGraphicsLines_var->isLineStrip(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |