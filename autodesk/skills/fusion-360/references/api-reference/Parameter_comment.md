# Parameter.comment Property

Parent Object: [Parameter](Parameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Parameter.h>

## Description

The comment associated with this parameter

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameter\_var" is a variable referencing a Parameter object. |

"parameter\_var" is a variable referencing a Parameter object. ```` ``` #include <Fusion/Fusion/Parameter.h>  // Get the value of the property. string propertyValue = parameter_var->comment();  // Set the value of the property, where value_var is a string. bool returnValue = parameter_var->comment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |