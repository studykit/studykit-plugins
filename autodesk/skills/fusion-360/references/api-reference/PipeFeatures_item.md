# PipeFeatures.item Method

Parent Object: [PipeFeatures](PipeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatures.h>

## Description

Function that returns the specified Pipe feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatures\_var" is a variable referencing a [PipeFeatures](PipeFeatures.htm) object.```` ``` returnValue = pipeFeatures_var.item(index) ``` ```` |

"pipeFeatures\_var" is a variable referencing a [PipeFeatures](PipeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PipeFeature](PipeFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |