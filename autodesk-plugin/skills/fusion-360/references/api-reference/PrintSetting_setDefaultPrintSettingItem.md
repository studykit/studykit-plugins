# PrintSetting.setDefaultPrintSettingItem Method

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

Defaults the PrintSetting item of the specified body preset. Throws exception when name not found.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object.```` ``` returnValue = printSetting_var.setDefaultPrintSettingItem(name) ``` ```` |

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The body preset id of the parameters that has to be defaulted. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |