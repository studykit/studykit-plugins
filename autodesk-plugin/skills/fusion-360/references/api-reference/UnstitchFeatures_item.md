# UnstitchFeatures.item Method

Parent Object: [UnstitchFeatures](UnstitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeatures.h>

## Description

Function that returns the specified Unstitch feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeatures\_var" is a variable referencing a [UnstitchFeatures](UnstitchFeatures.htm) object.```` ``` returnValue = unstitchFeatures_var.item(index) ``` ```` |

"unstitchFeatures\_var" is a variable referencing a [UnstitchFeatures](UnstitchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UnstitchFeature](UnstitchFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |