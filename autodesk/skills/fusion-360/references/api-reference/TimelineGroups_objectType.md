# TimelineGroups.objectType Property

Parent Object: [TimelineGroups](TimelineGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroups.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroups\_var" is a variable referencing a TimelineGroups object.  ```` ``` # Get the value of the property. propertyValue = timelineGroups_var.objectType ``` ```` |

"timelineGroups\_var" is a variable referencing a TimelineGroups object. ```` ``` #include <Fusion/Fusion/TimelineGroups.h>  // Get the value of the property. string propertyValue = timelineGroups_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |