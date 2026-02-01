# EventArgs.objectType Property

Parent Object: [EventArgs](EventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/EventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"eventArgs\_var" is a variable referencing an EventArgs object.  ```` ``` # Get the value of the property. propertyValue = eventArgs_var.objectType ``` ```` |

"eventArgs\_var" is a variable referencing an EventArgs object. ```` ``` #include <Core/Application/EventArgs.h>  // Get the value of the property. string propertyValue = eventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |