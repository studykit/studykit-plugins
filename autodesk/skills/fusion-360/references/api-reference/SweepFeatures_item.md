# SweepFeatures.item Method

Parent Object: [SweepFeatures](SweepFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatures.h>

## Description

Function that returns the specified sweep feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatures\_var" is a variable referencing a [SweepFeatures](SweepFeatures.htm) object.```` ``` returnValue = sweepFeatures_var.item(index) ``` ```` |

"sweepFeatures\_var" is a variable referencing a [SweepFeatures](SweepFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SweepFeature](SweepFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |