# CustomGraphicsText.size Property

Parent Object: [CustomGraphicsText](CustomGraphicsText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsText.h>

## Description

Gets and sets the size of the text in centimeters. This is the default size and applies to all of text unless there is a size override defined within the text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. |

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. ```` ``` #include <Fusion/Graphics/CustomGraphicsText.h>  // Get the value of the property. double propertyValue = customGraphicsText_var->size();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsText_var->size(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |