# RevolveFeatures.item Method

Parent Object: [RevolveFeatures](RevolveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatures.h>

## Description

Function that returns the specified revolve feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatures\_var" is a variable referencing a [RevolveFeatures](RevolveFeatures.htm) object.```` ``` returnValue = revolveFeatures_var.item(index) ``` ```` |

"revolveFeatures\_var" is a variable referencing a [RevolveFeatures](RevolveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RevolveFeature](RevolveFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |