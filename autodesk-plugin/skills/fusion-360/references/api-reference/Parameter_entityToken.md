# Parameter.entityToken Property

Parent Object: [Parameter](Parameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Parameter.h>

## Description

Returns a token for the Parameter object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameter\_var" is a variable referencing a Parameter object.  ```` ``` # Get the value of the property. propertyValue = parameter_var.entityToken ``` ```` |

"parameter\_var" is a variable referencing a Parameter object. ```` ``` #include <Fusion/Fusion/Parameter.h>  // Get the value of the property. string propertyValue = parameter_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |