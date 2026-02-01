# ModelParameter.entityToken Property

Parent Object: [ModelParameter](ModelParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameter.h>

## Description

Returns a token for the Parameter object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameter\_var" is a variable referencing a ModelParameter object.  ```` ``` # Get the value of the property. propertyValue = modelParameter_var.entityToken ``` ```` |

"modelParameter\_var" is a variable referencing a ModelParameter object. ```` ``` #include <Fusion/Fusion/ModelParameter.h>  // Get the value of the property. string propertyValue = modelParameter_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |