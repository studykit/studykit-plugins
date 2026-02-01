# CAM.generateTemplateXML Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Generates a template for the specified Operations, Setups, or Folders and returns the template as an XML string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` returnValue = cAM_var.generateTemplateXML(operations) ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the template XML as a string. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operations | [Base](Base.htm) | An Operation, Setup or Folder object from which to generate the template. You can also specify a collection of any combination of these object types. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |