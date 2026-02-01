# PipeFeatures.createInput Method

Parent Object: [PipeFeatures](PipeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatures.h>

## Description

Creates a PipeFeatureInput object for defining a simple Pipe feature with only a path. Use properties and methods on this object to define the Pipe you want to create and then use the Add method, passing in the PipeFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatures\_var" is a variable referencing a [PipeFeatures](PipeFeatures.htm) object.```` ``` returnValue = pipeFeatures_var.createInput(path, operation) ``` ```` |

"pipeFeatures\_var" is a variable referencing a [PipeFeatures](PipeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PipeFeatureInput](PipeFeatureInput.htm) | Returns the newly created PipeFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| path | [Path](Path.htm) | The path to create the Pipe. |
| operation | [FeatureOperations](FeatureOperations.htm) | The feature operation to perform. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |