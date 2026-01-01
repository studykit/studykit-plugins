# PrintSetting.duplicatePrintSettingItem Method

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

Duplicates the PrintSetting item of the specified body preset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object.```` ``` returnValue = printSetting_var.duplicatePrintSettingItem(name) ``` ```` |

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PrintSettingItem](PrintSettingItem.htm) | Returns the specified parameters or throws exception in the case where there is no parameters with the specified id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The body preset id of the parameters that has to be duplicated. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |