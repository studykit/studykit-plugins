# CAM.getMachiningTime Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Get the machining time for the specified objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` returnValue = cAM_var.getMachiningTime(operations, feedScale, rapidFeed, toolChangeTime) ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachiningTime](MachiningTime.htm) | Returns a MachiningTime object that has properties holding the calculation results. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operations | [Base](Base.htm) | An Operation, Setup, Folder, or Pattern object. You can also use an ObjectCollection to specify multiple objects of any of the supported types. |
| feedScale | double | The feed scale value (%) to use. |
| rapidFeed | double | The rapid feed rate in centimeters per second. |
| toolChangeTime | double | The tool change time in seconds. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |