# PrintSetting.deletePrintSettingItem Method

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

Deletes the PrintSettingItem of the specified body preset. Throws an exception when the name does not match any available PrintSettingItems or when trying to delete the default PrintSettingItem.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object.```` ``` returnValue = printSetting_var.deletePrintSettingItem(name) ``` ```` |

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The body preset id of the parameters that has to be deleted. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |