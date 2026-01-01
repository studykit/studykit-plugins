# PostProcessInput.programComment Property

Parent Object: [PostProcessInput](PostProcessInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/PostProcessInput.h>

## Description

Gets and sets the program comment. The default value for this property is an empty string ("").

## Syntax

* [Python](#Python)
* [C++](#C++)

"postProcessInput\_var" is a variable referencing a PostProcessInput object. |

"postProcessInput\_var" is a variable referencing a PostProcessInput object. ```` ``` #include <Cam/CAM/PostProcessInput.h>  // Get the value of the property. string propertyValue = postProcessInput_var->programComment();  // Set the value of the property, where value_var is a string. bool returnValue = postProcessInput_var->programComment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |