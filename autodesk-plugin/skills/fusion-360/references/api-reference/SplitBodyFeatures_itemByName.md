# SplitBodyFeatures.itemByName Method

Parent Object: [SplitBodyFeatures](SplitBodyFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeatures.h>

## Description

Function that returns the specified split body feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeatures\_var" is a variable referencing a [SplitBodyFeatures](SplitBodyFeatures.htm) object.```` ``` returnValue = splitBodyFeatures_var.itemByName(name) ``` ```` |

"splitBodyFeatures\_var" is a variable referencing a [SplitBodyFeatures](SplitBodyFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SplitBodyFeature](SplitBodyFeature.htm) | Returns the specified item or null if the specified name was not found. |

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