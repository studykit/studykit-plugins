# ChamferFeatures.itemByName Method

Parent Object: [ChamferFeatures](ChamferFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatures.h>

## Description

Function that returns the specified chamfer feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object.```` ``` returnValue = chamferFeatures_var.itemByName(name) ``` ```` |

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ChamferFeature](ChamferFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |