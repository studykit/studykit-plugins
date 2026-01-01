# TimelineGroup.entity Property

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

Returns the entity associated with this timeline object. Edit operations can be performed by getting the object representing the associated entity and using the methods and properties on that entity to make changes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a TimelineGroup object.  ```` ``` # Get the value of the property. propertyValue = timelineGroup_var.entity ``` ```` |

"timelineGroup\_var" is a variable referencing a TimelineGroup object. ```` ``` #include <Fusion/Fusion/TimelineGroup.h>  // Get the value of the property. Ptr<Base> propertyValue = timelineGroup_var->entity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |