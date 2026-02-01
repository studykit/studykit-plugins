# RipFeatures.item Method

Parent Object: [RipFeatures](RipFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatures.h>

## Description

Function that returns the specified Rip feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatures\_var" is a variable referencing a [RipFeatures](RipFeatures.htm) object.```` ``` returnValue = ripFeatures_var.item(index) ``` ```` |

"ripFeatures\_var" is a variable referencing a [RipFeatures](RipFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RipFeature](RipFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |