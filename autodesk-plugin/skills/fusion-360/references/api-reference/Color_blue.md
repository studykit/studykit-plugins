# Color.blue Property

Parent Object: [Color](Color.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Color.h>

## Description

Gets and sets the blue component of the color. The value can be 0 to 255.

## Syntax

* [Python](#Python)
* [C++](#C++)

"color\_var" is a variable referencing a Color object. |

"color\_var" is a variable referencing a Color object. ```` ``` #include <Core/Application/Color.h>  // Get the value of the property. short propertyValue = color_var->blue();  // Set the value of the property, where value_var is a short. bool returnValue = color_var->blue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a short.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |