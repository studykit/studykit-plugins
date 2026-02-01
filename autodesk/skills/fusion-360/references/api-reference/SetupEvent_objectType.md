# SetupEvent.objectType Property

Parent Object: [SetupEvent](SetupEvent.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEvent\_var" is a variable referencing a SetupEvent object.  ```` ``` # Get the value of the property. propertyValue = setupEvent_var.objectType ``` ```` |

"setupEvent\_var" is a variable referencing a SetupEvent object. ```` ``` #include <Cam/CAM/SetupEvent.h>  // Get the value of the property. string propertyValue = setupEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |