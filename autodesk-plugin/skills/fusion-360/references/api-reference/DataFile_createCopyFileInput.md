# DataFile.createCopyFileInput Method![](../images/TestTubeLarge.png)

Parent Object: [DataFile](DataFile.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Creates a new CopyFileInput object that is used to create a copy of any DataFile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object.```` ``` returnValue = dataFile_var.createCopyFileInput(folder) ``` ```` |

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CopyFileInput](CopyFileInput.htm) | Returns the created CopyFileInput object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| folder | [DataFolder](DataFolder.htm) | The folder where the copied file will be created. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |