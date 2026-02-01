# CoilFeatures.itemByName Method

Parent Object: [CoilFeatures](CoilFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeatures.h>

## Description

Function that returns the specified coil feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeatures\_var" is a variable referencing a [CoilFeatures](CoilFeatures.htm) object.```` ``` returnValue = coilFeatures_var.itemByName(name) ``` ```` |

"coilFeatures\_var" is a variable referencing a [CoilFeatures](CoilFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CoilFeature](CoilFeature.htm) | Returns the specified item or null if the specified name was not found. |

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