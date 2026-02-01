# DataEventArgs.objectType Property

Parent Object: [DataEventArgs](DataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEventArgs\_var" is a variable referencing a DataEventArgs object.  ```` ``` # Get the value of the property. propertyValue = dataEventArgs_var.objectType ``` ```` |

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. ```` ``` #include <Core/Dashboard/DataEventArgs.h>  // Get the value of the property. string propertyValue = dataEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |