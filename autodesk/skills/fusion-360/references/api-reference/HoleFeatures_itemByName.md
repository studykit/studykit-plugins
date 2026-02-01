# HoleFeatures.itemByName Method

Parent Object: [HoleFeatures](HoleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatures.h>

## Description

Function that returns the specified hole feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatures\_var" is a variable referencing a [HoleFeatures](HoleFeatures.htm) object.```` ``` returnValue = holeFeatures_var.itemByName(name) ``` ```` |

"holeFeatures\_var" is a variable referencing a [HoleFeatures](HoleFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [HoleFeature](HoleFeature.htm) | Returns the specified item or null if the specified name was not found. |

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