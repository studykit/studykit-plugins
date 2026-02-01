# CAMTemplateOperations.set Method![](../images/TestTubeLarge.png)

Parent Object: [CAMTemplateOperations](CAMTemplateOperations.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateOperations.h>

## Description

Set the element at the given index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateOperations\_var" is a variable referencing a [CAMTemplateOperations](CAMTemplateOperations.htm) object.```` ``` returnValue = cAMTemplateOperations_var.set(operationIndex, input) ``` ```` |

"cAMTemplateOperations\_var" is a variable referencing a [CAMTemplateOperations](CAMTemplateOperations.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operationIndex | integer | Index of the element to overwrite |
| input | [CAMTemplateOperationInput](CAMTemplateOperationInput.htm) | The element will be overwritten with a copy of this element. Must come from get() or makeInput(). |

## Version

Introduced in version March 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |