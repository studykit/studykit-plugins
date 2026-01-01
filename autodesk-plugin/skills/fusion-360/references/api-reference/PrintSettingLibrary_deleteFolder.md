# PrintSettingLibrary.deleteFolder Method

Parent Object: [PrintSettingLibrary](PrintSettingLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingLibrary.h>

## Description

Delete folder by URL from the library. Any content of the folder will also be deleted. Throw an error if given URL does not point to a valid folder or the URL is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object.```` ``` returnValue = printSettingLibrary_var.deleteFolder(url) ``` ```` |

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if folder was deleted successfully, false otherwise |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the folder that should be removed. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |