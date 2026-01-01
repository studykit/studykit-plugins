# Timeline.markerPosition Property

Parent Object: [Timeline](Timeline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Timeline.h>

## Description

Gets and sets the current position of the marker where 0 is at the beginning of the timeline and the value of Timeline.count is the end of the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timeline\_var" is a variable referencing a Timeline object. |

"timeline\_var" is a variable referencing a Timeline object. ```` ``` #include <Fusion/Fusion/Timeline.h>  // Get the value of the property. integer propertyValue = timeline_var->markerPosition();  // Set the value of the property, where value_var is an integer. bool returnValue = timeline_var->markerPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |