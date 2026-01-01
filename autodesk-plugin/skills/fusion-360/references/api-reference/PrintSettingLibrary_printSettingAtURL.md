# PrintSettingLibrary.printSettingAtURL Method

Parent Object: [PrintSettingLibrary](PrintSettingLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingLibrary.h>

## Description

Get a specific PrintSetting by the given URL. Returns null if the URL does not exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object.```` ``` returnValue = printSettingLibrary_var.printSettingAtURL(url) ``` ```` |

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PrintSetting](PrintSetting.htm) | Returns the PrintSetting for a valid URL, returns null otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the PrintSetting to be loaded. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |