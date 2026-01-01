# DraftFeatures.itemByName Method

Parent Object: [DraftFeatures](DraftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatures.h>

## Description

Function that returns the specified draft feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatures\_var" is a variable referencing a [DraftFeatures](DraftFeatures.htm) object.```` ``` returnValue = draftFeatures_var.itemByName(name) ``` ```` |

"draftFeatures\_var" is a variable referencing a [DraftFeatures](DraftFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DraftFeature](DraftFeature.htm) | Returns the specified item or null if the specified name was not found. |

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