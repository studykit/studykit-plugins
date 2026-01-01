# Snapshot.timelineObject Property

Parent Object: [Snapshot](Snapshot.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Snapshot.h>

## Description

Returns the timeline object associated with this snapshot.

## Syntax

* [Python](#Python)
* [C++](#C++)

"snapshot\_var" is a variable referencing a Snapshot object. |

"snapshot\_var" is a variable referencing a Snapshot object. ```` ``` #include <Fusion/Fusion/Snapshot.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = snapshot_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |