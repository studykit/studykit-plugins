# CombineFeatures.itemByName Method

Parent Object: [CombineFeatures](CombineFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatures.h>

## Description

Function that returns the specified combine feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatures\_var" is a variable referencing a [CombineFeatures](CombineFeatures.htm) object.```` ``` returnValue = combineFeatures_var.itemByName(name) ``` ```` |

"combineFeatures\_var" is a variable referencing a [CombineFeatures](CombineFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CombineFeature](CombineFeature.htm) | Returns the specified item or null if the specified name was not found. |

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