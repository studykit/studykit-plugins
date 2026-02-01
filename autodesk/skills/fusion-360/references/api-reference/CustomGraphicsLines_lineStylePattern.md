# CustomGraphicsLines.lineStylePattern Property

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

The line style to apply to the line. The default is to draw a continuous line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. |

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. ```` ``` #include <Fusion/Graphics/CustomGraphicsLines.h>  // Get the value of the property. LineStylePatterns propertyValue = customGraphicsLines_var->lineStylePattern();  // Set the value of the property, where value_var is a LineStylePatterns. bool returnValue = customGraphicsLines_var->lineStylePattern(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LineStylePatterns](LineStylePatterns.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |