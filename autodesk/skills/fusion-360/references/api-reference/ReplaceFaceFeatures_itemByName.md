# ReplaceFaceFeatures.itemByName Method

Parent Object: [ReplaceFaceFeatures](ReplaceFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatures.h>

## Description

Function that returns the specified replace face feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeatures\_var" is a variable referencing a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm) object.```` ``` returnValue = replaceFaceFeatures_var.itemByName(name) ``` ```` |

"replaceFaceFeatures\_var" is a variable referencing a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ReplaceFaceFeature](ReplaceFaceFeature.htm) | Returns the specified item or null if the specified name was not found. |

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