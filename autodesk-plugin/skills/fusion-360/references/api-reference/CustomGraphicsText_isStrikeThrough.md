# CustomGraphicsText.isStrikeThrough Property

Parent Object: [CustomGraphicsText](CustomGraphicsText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsText.h>

## Description

Specifies that the text displays using a strike through style. This is the default strike through style and applies to all of text unless there is a style override defined within the text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. |

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. ```` ``` #include <Fusion/Graphics/CustomGraphicsText.h>  // Get the value of the property. boolean propertyValue = customGraphicsText_var->isStrikeThrough();  // Set the value of the property, where value_var is a boolean. bool returnValue = customGraphicsText_var->isStrikeThrough(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |