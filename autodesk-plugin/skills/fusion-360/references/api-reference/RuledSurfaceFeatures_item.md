# RuledSurfaceFeatures.item Method

Parent Object: [RuledSurfaceFeatures](RuledSurfaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatures.h>

## Description

Function that returns the specified ruled surface feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatures\_var" is a variable referencing a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm) object.```` ``` returnValue = ruledSurfaceFeatures_var.item(index) ``` ```` |

"ruledSurfaceFeatures\_var" is a variable referencing a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RuledSurfaceFeature](RuledSurfaceFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |