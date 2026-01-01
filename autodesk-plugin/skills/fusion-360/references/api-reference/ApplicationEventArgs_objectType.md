# ApplicationEventArgs.objectType Property

Parent Object: [ApplicationEventArgs](ApplicationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEventArgs\_var" is a variable referencing an ApplicationEventArgs object.  ```` ``` # Get the value of the property. propertyValue = applicationEventArgs_var.objectType ``` ```` |

"applicationEventArgs\_var" is a variable referencing an ApplicationEventArgs object. ```` ``` #include <Core/Application/ApplicationEventArgs.h>  // Get the value of the property. string propertyValue = applicationEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |