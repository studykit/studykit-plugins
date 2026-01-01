# ValueInput.objectType Property

Parent Object: [ValueInput](ValueInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ValueInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueInput\_var" is a variable referencing a ValueInput object.  ```` ``` # Get the value of the property. propertyValue = valueInput_var.objectType ``` ```` |

"valueInput\_var" is a variable referencing a ValueInput object. ```` ``` #include <Core/Application/ValueInput.h>  // Get the value of the property. string propertyValue = valueInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |