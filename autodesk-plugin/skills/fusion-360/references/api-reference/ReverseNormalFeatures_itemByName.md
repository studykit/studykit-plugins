# ReverseNormalFeatures.itemByName Method

Parent Object: [ReverseNormalFeatures](ReverseNormalFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeatures.h>

## Description

Function that returns the specified reverse normal feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeatures\_var" is a variable referencing a [ReverseNormalFeatures](ReverseNormalFeatures.htm) object.```` ``` returnValue = reverseNormalFeatures_var.itemByName(name) ``` ```` |

"reverseNormalFeatures\_var" is a variable referencing a [ReverseNormalFeatures](ReverseNormalFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ReverseNormalFeature](ReverseNormalFeature.htm) | Returns the specified item or null if the specified name was not found. |

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