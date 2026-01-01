# CustomGraphicsViewScale.pixelScale Property

Parent Object: [CustomGraphicsViewScale](CustomGraphicsViewScale.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsViewScale.h>

## Description

Gets and sets the scale of the custom graphics relative to the view. If a custom graphics line is defined to be 100 units long it would usually display as 100 cm long. When it is view scaled with a pixel scale of 1 it will display as 100 pixels long.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsViewScale\_var" is a variable referencing a CustomGraphicsViewScale object. |

"customGraphicsViewScale\_var" is a variable referencing a CustomGraphicsViewScale object. ```` ``` #include <Fusion/Graphics/CustomGraphicsViewScale.h>  // Get the value of the property. double propertyValue = customGraphicsViewScale_var->pixelScale();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsViewScale_var->pixelScale(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |