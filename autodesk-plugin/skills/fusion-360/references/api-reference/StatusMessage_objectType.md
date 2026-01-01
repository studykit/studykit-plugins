# StatusMessage.objectType Property

Parent Object: [StatusMessage](StatusMessage.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessage.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"statusMessage\_var" is a variable referencing a StatusMessage object.  ```` ``` # Get the value of the property. propertyValue = statusMessage_var.objectType ``` ```` |

"statusMessage\_var" is a variable referencing a StatusMessage object. ```` ``` #include <Core/Application/StatusMessage.h>  // Get the value of the property. string propertyValue = statusMessage_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |