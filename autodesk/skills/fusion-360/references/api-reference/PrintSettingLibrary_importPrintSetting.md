# PrintSettingLibrary.importPrintSetting Method

Parent Object: [PrintSettingLibrary](PrintSettingLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingLibrary.h>

## Description

Import a given PrintSetting at a specific location. The PrintSetting will be stored in the library. Throws an error if the given URL is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object.```` ``` returnValue = printSettingLibrary_var.importPrintSetting(printSetting, destinationUrl, printSettingName) ``` ```` |

"printSettingLibrary\_var" is a variable referencing a [PrintSettingLibrary](PrintSettingLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL of the newly imported PrintSetting, or null if the import failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| printSetting | [PrintSetting](PrintSetting.htm) | The PrintSetting that should be imported. |
| destinationUrl | [URL](URL.htm) | The URL to the folder where to save the PrintSetting. |
| printSettingName | string | The name that should be assigned to imported PrintSetting. The name can be extended if there already exists a PrintSetting at given location to ensure a unique name. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |