# CopyPasteBody.timelineObject Property

Parent Object: [CopyPasteBody](CopyPasteBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBody.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyPasteBody\_var" is a variable referencing a CopyPasteBody object. |

"copyPasteBody\_var" is a variable referencing a CopyPasteBody object. ```` ``` #include <Fusion/Features/CopyPasteBody.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = copyPasteBody_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |