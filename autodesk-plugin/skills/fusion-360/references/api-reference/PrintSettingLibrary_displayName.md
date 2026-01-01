# PrintSettingLibrary.displayName Method

Parent Object: [PrintSettingLibrary](PrintSettingLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingLibrary.h>

## Description

Get the localized display name for a given URL. The URL must point to a folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object.```` ``` returnValue = printSettingLibrary_var.displayName(url) ``` ```` |

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns localized display name for the folder. Returns empty string for invalid URL. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL that defines the path to a folder. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |