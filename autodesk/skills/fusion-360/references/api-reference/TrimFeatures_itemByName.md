# TrimFeatures.itemByName Method

Parent Object: [TrimFeatures](TrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatures.h>

## Description

Function that returns the specified trim feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatures\_var" is a variable referencing a [TrimFeatures](TrimFeatures.htm) object.```` ``` returnValue = trimFeatures_var.itemByName(name) ``` ```` |

"trimFeatures\_var" is a variable referencing a [TrimFeatures](TrimFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TrimFeature](TrimFeature.htm) | Returns the specified item or null if the specified name was not found. |

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