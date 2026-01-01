# PipeFeature.timelineObject Property

Parent Object: [PipeFeature](PipeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeature\_var" is a variable referencing a PipeFeature object. |

"pipeFeature\_var" is a variable referencing a PipeFeature object. ```` ``` #include <Fusion/Features/PipeFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = pipeFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |