# RigidGroup.timelineObject Property

Parent Object: [RigidGroup](RigidGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroup.h>

## Description

Returns the timeline object associated with this rigid group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroup\_var" is a variable referencing a RigidGroup object. |

"rigidGroup\_var" is a variable referencing a RigidGroup object. ```` ``` #include <Fusion/Components/RigidGroup.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = rigidGroup_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |