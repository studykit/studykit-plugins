# ExtrudeFeatures.item Method

Parent Object: [ExtrudeFeatures](ExtrudeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatures.h>

## Description

Function that returns the specified extrude feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatures\_var" is a variable referencing an [ExtrudeFeatures](ExtrudeFeatures.htm) object.```` ``` returnValue = extrudeFeatures_var.item(index) ``` ```` |

"extrudeFeatures\_var" is a variable referencing an [ExtrudeFeatures](ExtrudeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtrudeFeature](ExtrudeFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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