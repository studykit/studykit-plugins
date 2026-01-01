# MoveFeatures.itemByName Method

Parent Object: [MoveFeatures](MoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatures.h>

## Description

Function that returns the specified move feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object.```` ``` returnValue = moveFeatures_var.itemByName(name) ``` ```` |

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MoveFeature](MoveFeature.htm) | Returns the specified item or null if the specified name was not found. |

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