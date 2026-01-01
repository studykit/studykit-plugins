# UnfoldFeatures.item Method

Parent Object: [UnfoldFeatures](UnfoldFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/UnfoldFeatures.h>

## Description

Function that returns the specified unfold feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unfoldFeatures\_var" is a variable referencing a [UnfoldFeatures](UnfoldFeatures.htm) object.```` ``` returnValue = unfoldFeatures_var.item(index) ``` ```` |

"unfoldFeatures\_var" is a variable referencing a [UnfoldFeatures](UnfoldFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UnfoldFeature](UnfoldFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |