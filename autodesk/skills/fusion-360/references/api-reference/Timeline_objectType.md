# Timeline.objectType Property

Parent Object: [Timeline](Timeline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Timeline.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timeline\_var" is a variable referencing a Timeline object.  ```` ``` # Get the value of the property. propertyValue = timeline_var.objectType ``` ```` |

"timeline\_var" is a variable referencing a Timeline object. ```` ``` #include <Fusion/Fusion/Timeline.h>  // Get the value of the property. string propertyValue = timeline_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |