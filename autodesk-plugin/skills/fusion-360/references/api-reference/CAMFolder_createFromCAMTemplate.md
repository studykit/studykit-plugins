# CAMFolder.createFromCAMTemplate Method

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired. Please use createFromCAMTemplate2 in conjunction with a CreateFromCAMTemplateInput to create operations from a template file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a [CAMFolder](CAMFolder.htm) object.```` ``` returnValue = cAMFolder_var.createFromCAMTemplate(camTemplate) ``` ```` |

"cAMFolder\_var" is a variable referencing a [CAMFolder](CAMFolder.htm) object.  ```` ``` #include <Cam/CAM/CAMFolder.h>  returnValue = cAMFolder_var->createFromCAMTemplate(camTemplate); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OperationBase](OperationBase.htm)[] | Returns an array containing all of the operations, folders and patterns created from the template. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| camTemplate | [CAMTemplate](CAMTemplate.htm) | The CAMTemplate object to apply |

## Version

Introduced in version April 2023
Retired in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |