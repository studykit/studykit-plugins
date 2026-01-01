# CAM.generateAllToolpaths Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Generates or regenerates all the operations in the document, including those nested in sub-folders or patterns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` returnValue = cAM_var.generateAllToolpaths(skipValid) ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [GenerateToolpathFuture](GenerateToolpathFuture.htm) | Return GenerateToolpathFuture that includes the status of operation generation. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| skipValid | boolean | Option to skip valid operations and only regenerate invalid operations. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [CAM Parameter Modification API Sample](CAMParameterChange_Sample_Sample.htm) | Demonstrates changing parameters of existing toolpaths. |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |
| [Create CAM Operation From Template API Sample](New_Operation_Sample_Sample.htm) | Demonstrates adding a new toolpath into the document using an existing CAM template. You can view the template [here](../ExtraFiles/face.f3dhsm-template), although it will be loaded automatically. Run the sample script within any Fusion project containing at least one setup. A new facing operation will be created at the end of each setup discovered. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |