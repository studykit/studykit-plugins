# Documents.objectType Property

Parent Object: [Documents](Documents.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Documents.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documents\_var" is a variable referencing a Documents object.  ```` ``` # Get the value of the property. propertyValue = documents_var.objectType ``` ```` |

"documents\_var" is a variable referencing a Documents object. ```` ``` #include <Core/Application/Documents.h>  // Get the value of the property. string propertyValue = documents_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |