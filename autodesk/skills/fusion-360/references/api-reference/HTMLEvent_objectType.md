# HTMLEvent.objectType Property

Parent Object: [HTMLEvent](HTMLEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/HTMLEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"hTMLEvent\_var" is a variable referencing a HTMLEvent object.  ```` ``` # Get the value of the property. propertyValue = hTMLEvent_var.objectType ``` ```` |

"hTMLEvent\_var" is a variable referencing a HTMLEvent object. ```` ``` #include <Core/UserInterface/HTMLEvent.h>  // Get the value of the property. string propertyValue = hTMLEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |