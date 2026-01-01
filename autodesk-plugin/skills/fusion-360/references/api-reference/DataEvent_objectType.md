# DataEvent.objectType Property

Parent Object: [DataEvent](DataEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEvent\_var" is a variable referencing a DataEvent object.  ```` ``` # Get the value of the property. propertyValue = dataEvent_var.objectType ``` ```` |

"dataEvent\_var" is a variable referencing a DataEvent object. ```` ``` #include <Core/Dashboard/DataEvent.h>  // Get the value of the property. string propertyValue = dataEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |