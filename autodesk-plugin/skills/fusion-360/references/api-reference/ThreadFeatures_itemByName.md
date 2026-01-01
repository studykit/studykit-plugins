# ThreadFeatures.itemByName Method

Parent Object: [ThreadFeatures](ThreadFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatures.h>

## Description

Function that returns the specified thread feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatures\_var" is a variable referencing a [ThreadFeatures](ThreadFeatures.htm) object.```` ``` returnValue = threadFeatures_var.itemByName(name) ``` ```` |

"threadFeatures\_var" is a variable referencing a [ThreadFeatures](ThreadFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThreadFeature](ThreadFeature.htm) | Returns the specified item or null if the specified name was not found. |

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