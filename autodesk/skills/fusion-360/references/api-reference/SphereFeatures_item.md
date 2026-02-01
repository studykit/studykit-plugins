# SphereFeatures.item Method

Parent Object: [SphereFeatures](SphereFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SphereFeatures.h>

## Description

Function that returns the specified sphere feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphereFeatures\_var" is a variable referencing a [SphereFeatures](SphereFeatures.htm) object.```` ``` returnValue = sphereFeatures_var.item(index) ``` ```` |

"sphereFeatures\_var" is a variable referencing a [SphereFeatures](SphereFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SphereFeature](SphereFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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