# WebRequestEvent.objectType Property

Parent Object: [WebRequestEvent](WebRequestEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webRequestEvent\_var" is a variable referencing a WebRequestEvent object.  ```` ``` # Get the value of the property. propertyValue = webRequestEvent_var.objectType ``` ```` |

"webRequestEvent\_var" is a variable referencing a WebRequestEvent object. ```` ``` #include <Core/Application/WebRequestEvent.h>  // Get the value of the property. string propertyValue = webRequestEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |