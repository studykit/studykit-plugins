# CustomGraphicsLines.isVisible Property

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

Gets and sets if the graphics entity is visible in the graphics window. By default, when a new entity is created it is visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. |

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. ```` ``` #include <Fusion/Graphics/CustomGraphicsLines.h>  // Get the value of the property. boolean propertyValue = customGraphicsLines_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = customGraphicsLines_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |