# CAMPattern.createFromTemplate Method

Parent Object: [CAMPattern](CAMPattern.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPattern.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired. Please use createFromCAMTemplate2 in conjunction with a CreateFromCAMTemplateInput to create operations from a template file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPattern\_var" is a variable referencing a [CAMPattern](CAMPattern.htm) object.```` ``` returnValue = cAMPattern_var.createFromTemplate(templateFilePath) ``` ```` |

"cAMPattern\_var" is a variable referencing a [CAMPattern](CAMPattern.htm) object.  ```` ``` #include <Cam/CAM/CAMPattern.h>  returnValue = cAMPattern_var->createFromTemplate(templateFilePath); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns the collection containing all of the operations, folders and patterns created from the template file. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| templateFilePath | string | The full path to the template file. |

## Version

Introduced in version May 2020
Retired in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |