# PipeFeatures.itemByName Method

Parent Object: [PipeFeatures](PipeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatures.h>

## Description

Function that returns the specified Pipe feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatures\_var" is a variable referencing a [PipeFeatures](PipeFeatures.htm) object.```` ``` returnValue = pipeFeatures_var.itemByName(name) ``` ```` |

"pipeFeatures\_var" is a variable referencing a [PipeFeatures](PipeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PipeFeature](PipeFeature.htm) | Returns the specified item or null if the specified name was not found. |

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