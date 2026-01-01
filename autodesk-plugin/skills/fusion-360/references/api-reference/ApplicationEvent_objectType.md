# ApplicationEvent.objectType Property

Parent Object: [ApplicationEvent](ApplicationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEvent\_var" is a variable referencing an ApplicationEvent object.  ```` ``` # Get the value of the property. propertyValue = applicationEvent_var.objectType ``` ```` |

"applicationEvent\_var" is a variable referencing an ApplicationEvent object. ```` ``` #include <Core/Application/ApplicationEvent.h>  // Get the value of the property. string propertyValue = applicationEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |