# CylinderFeatures.item Method

Parent Object: [CylinderFeatures](CylinderFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CylinderFeatures.h>

## Description

Function that returns the specified cylinder feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinderFeatures\_var" is a variable referencing a [CylinderFeatures](CylinderFeatures.htm) object.```` ``` returnValue = cylinderFeatures_var.item(index) ``` ```` |

"cylinderFeatures\_var" is a variable referencing a [CylinderFeatures](CylinderFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CylinderFeature](CylinderFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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