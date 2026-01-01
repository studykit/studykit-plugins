# CutPasteBody.timelineObject Property

Parent Object: [CutPasteBody](CutPasteBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CutPasteBody.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cutPasteBody\_var" is a variable referencing a CutPasteBody object. |

"cutPasteBody\_var" is a variable referencing a CutPasteBody object. ```` ``` #include <Fusion/Features/CutPasteBody.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = cutPasteBody_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |