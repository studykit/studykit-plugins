# SilhouetteSplitFeatures.item Method

Parent Object: [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatures.h>

## Description

Function that returns the specified silhouette split feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatures\_var" is a variable referencing a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm) object.```` ``` returnValue = silhouetteSplitFeatures_var.item(index) ``` ```` |

"silhouetteSplitFeatures\_var" is a variable referencing a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SilhouetteSplitFeature](SilhouetteSplitFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |