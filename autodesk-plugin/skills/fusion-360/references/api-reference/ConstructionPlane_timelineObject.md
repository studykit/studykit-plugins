# ConstructionPlane.timelineObject Property

Parent Object: [ConstructionPlane](ConstructionPlane.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlane.h>

## Description

Returns the timeline object associated with this construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. |

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. ```` ``` #include <Fusion/Construction/ConstructionPlane.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = constructionPlane_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |