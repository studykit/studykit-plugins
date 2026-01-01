# DocumentEventArgs.objectType Property

Parent Object: [DocumentEventArgs](DocumentEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object.  ```` ``` # Get the value of the property. propertyValue = documentEventArgs_var.objectType ``` ```` |

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. ```` ``` #include <Core/Application/DocumentEventArgs.h>  // Get the value of the property. string propertyValue = documentEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |