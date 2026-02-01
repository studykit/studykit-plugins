# CAMPattern.createFromCAMTemplate2 Method

Parent Object: [CAMPattern](CAMPattern.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPattern.h>

## Description

Create new operations, folders, or patterns from the specified CAMTemplate. They are added to the end of the parent setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPattern\_var" is a variable referencing a [CAMPattern](CAMPattern.htm) object.```` ``` returnValue = cAMPattern_var.createFromCAMTemplate2(input) ``` ```` |

"cAMPattern\_var" is a variable referencing a [CAMPattern](CAMPattern.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OperationBase](OperationBase.htm)[] | Returns an array containing all of the operations, folders and patterns created from the template. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [CreateFromCAMTemplateInput](CreateFromCAMTemplateInput.htm) | Input object that contains the template to create from and the generation mode. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |