# Setup.createFromTemplateXML Method

Parent Object: [Setup](Setup.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired. Please use createFromCAMTemplate2 in conjunction with a CreateFromCAMTemplateInput to create operations from a template file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a [Setup](Setup.htm) object.```` ``` returnValue = setup_var.createFromTemplateXML(templateXML) ``` ```` |

"setup\_var" is a variable referencing a [Setup](Setup.htm) object.  ```` ``` #include <Cam/CAM/Setup.h>  returnValue = setup_var->createFromTemplateXML(templateXML); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OperationBase](OperationBase.htm)[] | Returns an array containing all of the operations, folders and patterns created from the template. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| templateXML | string | The full XML content of the template. |

## Version

Introduced in version April 2023
Retired in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |