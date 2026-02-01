# RibFeatures.item Method

Parent Object: [RibFeatures](RibFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RibFeatures.h>

## Description

Function that returns the specified Rib feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ribFeatures\_var" is a variable referencing a [RibFeatures](RibFeatures.htm) object.```` ``` returnValue = ribFeatures_var.item(index) ``` ```` |

"ribFeatures\_var" is a variable referencing a [RibFeatures](RibFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RibFeature](RibFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |