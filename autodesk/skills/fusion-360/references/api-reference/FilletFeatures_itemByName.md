# FilletFeatures.itemByName Method

Parent Object: [FilletFeatures](FilletFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatures.h>

## Description

Function that returns the specified fillet feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatures\_var" is a variable referencing a [FilletFeatures](FilletFeatures.htm) object.```` ``` returnValue = filletFeatures_var.itemByName(name) ``` ```` |

"filletFeatures\_var" is a variable referencing a [FilletFeatures](FilletFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FilletFeature](FilletFeature.htm) | Returns the specified item or null if the specified name was not found. |

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