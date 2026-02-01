# UnstitchFeatures.itemByName Method

Parent Object: [UnstitchFeatures](UnstitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeatures.h>

## Description

Function that returns the specified unstitch feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeatures\_var" is a variable referencing a [UnstitchFeatures](UnstitchFeatures.htm) object.```` ``` returnValue = unstitchFeatures_var.itemByName(name) ``` ```` |

"unstitchFeatures\_var" is a variable referencing a [UnstitchFeatures](UnstitchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UnstitchFeature](UnstitchFeature.htm) | Returns the specified item or null if the specified name was not found. |

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