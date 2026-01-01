# TorusFeatures.itemByName Method

Parent Object: [TorusFeatures](TorusFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TorusFeatures.h>

## Description

Function that returns the specified torus feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torusFeatures\_var" is a variable referencing a [TorusFeatures](TorusFeatures.htm) object.```` ``` returnValue = torusFeatures_var.itemByName(name) ``` ```` |

"torusFeatures\_var" is a variable referencing a [TorusFeatures](TorusFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TorusFeature](TorusFeature.htm) | Returns the specified item or null if the specified name was not found. |

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