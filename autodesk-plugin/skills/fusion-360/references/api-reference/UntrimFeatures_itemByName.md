# UntrimFeatures.itemByName Method

Parent Object: [UntrimFeatures](UntrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatures.h>

## Description

Function that returns the specified Untrim feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatures\_var" is a variable referencing a [UntrimFeatures](UntrimFeatures.htm) object.```` ``` returnValue = untrimFeatures_var.itemByName(name) ``` ```` |

"untrimFeatures\_var" is a variable referencing a [UntrimFeatures](UntrimFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UntrimFeature](UntrimFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |