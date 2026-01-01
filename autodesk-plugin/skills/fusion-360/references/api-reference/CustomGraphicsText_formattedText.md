# CustomGraphicsText.formattedText Property

Parent Object: [CustomGraphicsText](CustomGraphicsText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsText.h>

## Description

Gets and sets the formatted text definition. This is the full string, including the formatting information, that's used to define the displayed text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. |

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. ```` ``` #include <Fusion/Graphics/CustomGraphicsText.h>  // Get the value of the property. string propertyValue = customGraphicsText_var->formattedText();  // Set the value of the property, where value_var is a string. bool returnValue = customGraphicsText_var->formattedText(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |