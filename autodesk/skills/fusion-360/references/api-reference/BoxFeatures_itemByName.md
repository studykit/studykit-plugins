# BoxFeatures.itemByName Method

Parent Object: [BoxFeatures](BoxFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeatures.h>

## Description

Function that returns the specified box feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeatures\_var" is a variable referencing a [BoxFeatures](BoxFeatures.htm) object.```` ``` returnValue = boxFeatures_var.itemByName(name) ``` ```` |

"boxFeatures\_var" is a variable referencing a [BoxFeatures](BoxFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoxFeature](BoxFeature.htm) | Returns the specified item or null if the specified name was not found. |

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