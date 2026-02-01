# ThickenFeatures.itemByName Method

Parent Object: [ThickenFeatures](ThickenFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatures.h>

## Description

Function that returns the specified thicken feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatures\_var" is a variable referencing a [ThickenFeatures](ThickenFeatures.htm) object.```` ``` returnValue = thickenFeatures_var.itemByName(name) ``` ```` |

"thickenFeatures\_var" is a variable referencing a [ThickenFeatures](ThickenFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThickenFeature](ThickenFeature.htm) | Returns the specified item or null if the specified name was not found. |

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