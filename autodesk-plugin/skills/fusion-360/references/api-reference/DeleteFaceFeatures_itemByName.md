# DeleteFaceFeatures.itemByName Method

Parent Object: [DeleteFaceFeatures](DeleteFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DeleteFaceFeatures.h>

## Description

Function that returns the specified DeleteFaceFeature object using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"deleteFaceFeatures\_var" is a variable referencing a [DeleteFaceFeatures](DeleteFaceFeatures.htm) object.```` ``` returnValue = deleteFaceFeatures_var.itemByName(name) ``` ```` |

"deleteFaceFeatures\_var" is a variable referencing a [DeleteFaceFeatures](DeleteFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DeleteFaceFeature](DeleteFaceFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |