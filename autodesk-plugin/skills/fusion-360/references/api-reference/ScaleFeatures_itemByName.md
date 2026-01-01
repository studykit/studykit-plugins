# ScaleFeatures.itemByName Method

Parent Object: [ScaleFeatures](ScaleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatures.h>

## Description

Function that returns the specified scale feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatures\_var" is a variable referencing a [ScaleFeatures](ScaleFeatures.htm) object.```` ``` returnValue = scaleFeatures_var.itemByName(name) ``` ```` |

"scaleFeatures\_var" is a variable referencing a [ScaleFeatures](ScaleFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ScaleFeature](ScaleFeature.htm) | Returns the specified item or null if the specified name was not found. |

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