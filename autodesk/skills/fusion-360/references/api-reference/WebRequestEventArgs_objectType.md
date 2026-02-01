# WebRequestEventArgs.objectType Property

Parent Object: [WebRequestEventArgs](WebRequestEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webRequestEventArgs\_var" is a variable referencing a WebRequestEventArgs object.  ```` ``` # Get the value of the property. propertyValue = webRequestEventArgs_var.objectType ``` ```` |

"webRequestEventArgs\_var" is a variable referencing a WebRequestEventArgs object. ```` ``` #include <Core/Application/WebRequestEventArgs.h>  // Get the value of the property. string propertyValue = webRequestEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |