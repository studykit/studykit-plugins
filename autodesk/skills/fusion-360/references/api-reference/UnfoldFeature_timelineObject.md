# UnfoldFeature.timelineObject Property

Parent Object: [UnfoldFeature](UnfoldFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/UnfoldFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unfoldFeature\_var" is a variable referencing a UnfoldFeature object. |

"unfoldFeature\_var" is a variable referencing a UnfoldFeature object. ```` ``` #include <Fusion/SheetMetal/UnfoldFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = unfoldFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |