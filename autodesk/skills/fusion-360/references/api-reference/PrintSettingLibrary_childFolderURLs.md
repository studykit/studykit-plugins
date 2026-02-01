# PrintSettingLibrary.childFolderURLs Method

Parent Object: [PrintSettingLibrary](PrintSettingLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingLibrary.h>

## Description

Get all library folders under given URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object.```` ``` returnValue = printSettingLibrary_var.childFolderURLs(url) ``` ```` |

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm)[] | Returns list of folder URLs at given location. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the parent folder. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |