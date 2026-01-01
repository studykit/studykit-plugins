# Timeline.item Method

Parent Object: [Timeline](Timeline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Timeline.h>

## Description

Function that returns the specified item in the timeline using an index into the collection. The items are returned in the order they appear in the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timeline\_var" is a variable referencing a [Timeline](Timeline.htm) object.```` ``` returnValue = timeline_var.item(index) ``` ```` |

"timeline\_var" is a variable referencing a [Timeline](Timeline.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TimelineObject](TimelineObject.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [Ruled Surface Feature API Sample](RuledSurfaceFeatureSample_Sample.htm) | Demonstrates creating a new ruled surface feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |