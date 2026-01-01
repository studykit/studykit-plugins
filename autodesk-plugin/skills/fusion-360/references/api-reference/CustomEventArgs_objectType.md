# CustomEventArgs.objectType Property

Parent Object: [CustomEventArgs](CustomEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEventArgs\_var" is a variable referencing a CustomEventArgs object.  ```` ``` # Get the value of the property. propertyValue = customEventArgs_var.objectType ``` ```` |

"customEventArgs\_var" is a variable referencing a CustomEventArgs object. ```` ``` #include <Core/Application/CustomEventArgs.h>  // Get the value of the property. string propertyValue = customEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |