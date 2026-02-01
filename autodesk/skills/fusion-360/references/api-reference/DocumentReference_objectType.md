# DocumentReference.objectType Property

Parent Object: [DocumentReference](DocumentReference.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReference.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentReference\_var" is a variable referencing a DocumentReference object.  ```` ``` # Get the value of the property. propertyValue = documentReference_var.objectType ``` ```` |

"documentReference\_var" is a variable referencing a DocumentReference object. ```` ``` #include <Core/Application/DocumentReference.h>  // Get the value of the property. string propertyValue = documentReference_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |