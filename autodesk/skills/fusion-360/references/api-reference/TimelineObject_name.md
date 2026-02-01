# TimelineObject.name Property

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Gets and sets the name of this timeline object. This name is shared by the object the timeline object represents. For example, if the TimelineObject represents a Sketch and you change the name using the TimelineObject, the name of the sketch in the browser is also changed. The reverse is also true. Setting the name of an object; sketch, feature construction geometry, etc, will also change the name of the associated node in the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a TimelineObject object. |

"timelineObject\_var" is a variable referencing a TimelineObject object. ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Get the value of the property. string propertyValue = timelineObject_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = timelineObject_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |