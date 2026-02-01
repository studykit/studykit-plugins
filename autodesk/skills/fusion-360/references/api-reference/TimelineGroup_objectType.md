# TimelineGroup.objectType Property

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a TimelineGroup object.  ```` ``` # Get the value of the property. propertyValue = timelineGroup_var.objectType ``` ```` |

"timelineGroup\_var" is a variable referencing a TimelineGroup object. ```` ``` #include <Fusion/Fusion/TimelineGroup.h>  // Get the value of the property. string propertyValue = timelineGroup_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |