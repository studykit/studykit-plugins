# PatchFeatures.itemByName Method

Parent Object: [PatchFeatures](PatchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatures.h>

## Description

Function that returns the specified patch feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatures\_var" is a variable referencing a [PatchFeatures](PatchFeatures.htm) object.```` ``` returnValue = patchFeatures_var.itemByName(name) ``` ```` |

"patchFeatures\_var" is a variable referencing a [PatchFeatures](PatchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PatchFeature](PatchFeature.htm) | Returns the specified item or null if the specified name was not found. |

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