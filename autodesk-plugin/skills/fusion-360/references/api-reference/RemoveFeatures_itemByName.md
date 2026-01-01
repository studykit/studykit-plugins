# RemoveFeatures.itemByName Method

Parent Object: [RemoveFeatures](RemoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeatures.h>

## Description

Function that returns the specified remove feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeatures\_var" is a variable referencing a [RemoveFeatures](RemoveFeatures.htm) object.```` ``` returnValue = removeFeatures_var.itemByName(name) ``` ```` |

"removeFeatures\_var" is a variable referencing a [RemoveFeatures](RemoveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RemoveFeature](RemoveFeature.htm) | Returns the specified item or null if the specified name was not found. |

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