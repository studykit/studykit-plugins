# ExtendFeatures.itemByName Method

Parent Object: [ExtendFeatures](ExtendFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatures.h>

## Description

Function that returns the specified extend feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatures\_var" is a variable referencing an [ExtendFeatures](ExtendFeatures.htm) object.```` ``` returnValue = extendFeatures_var.itemByName(name) ``` ```` |

"extendFeatures\_var" is a variable referencing an [ExtendFeatures](ExtendFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtendFeature](ExtendFeature.htm) | Returns the specified item or null if the specified name was not found. |

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