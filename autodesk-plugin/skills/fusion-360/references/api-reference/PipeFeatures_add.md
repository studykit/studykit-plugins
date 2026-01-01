# PipeFeatures.add Method

Parent Object: [PipeFeatures](PipeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatures.h>

## Description

Creates a new Pipe feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatures\_var" is a variable referencing a [PipeFeatures](PipeFeatures.htm) object.```` ``` returnValue = pipeFeatures_var.add(input) ``` ```` |

"pipeFeatures\_var" is a variable referencing a [PipeFeatures](PipeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PipeFeature](PipeFeature.htm) | Returns the newly created PipeFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [PipeFeatureInput](PipeFeatureInput.htm) | A PipeFeatureInput object that defines the desired Pipe. Use the createInput method to create a new PipeFeatureInput object and then use methods on it (the PipeFeatureInput object) to define the Pipe. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |