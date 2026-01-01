# ThickenFeatures.item Method

Parent Object: [ThickenFeatures](ThickenFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatures.h>

## Description

Function that returns the specified Thicken feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatures\_var" is a variable referencing a [ThickenFeatures](ThickenFeatures.htm) object.```` ``` returnValue = thickenFeatures_var.item(index) ``` ```` |

"thickenFeatures\_var" is a variable referencing a [ThickenFeatures](ThickenFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThickenFeature](ThickenFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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