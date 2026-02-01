# FlangeFeatures.item Method

Parent Object: [FlangeFeatures](FlangeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlangeFeatures.h>

## Description

Function that returns the specified flange feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flangeFeatures\_var" is a variable referencing a [FlangeFeatures](FlangeFeatures.htm) object.```` ``` returnValue = flangeFeatures_var.item(index) ``` ```` |

"flangeFeatures\_var" is a variable referencing a [FlangeFeatures](FlangeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FlangeFeature](FlangeFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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