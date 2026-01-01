# MirrorFeatures.item Method

Parent Object: [MirrorFeatures](MirrorFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatures.h>

## Description

Function that returns the specified mirror feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatures\_var" is a variable referencing a [MirrorFeatures](MirrorFeatures.htm) object.```` ``` returnValue = mirrorFeatures_var.item(index) ``` ```` |

"mirrorFeatures\_var" is a variable referencing a [MirrorFeatures](MirrorFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MirrorFeature](MirrorFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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