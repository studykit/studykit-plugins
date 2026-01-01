# DataFile.download Method

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Performs a synchronous or asynchronous download of this DataFile. Only DataFiles that represent non-Fusion data can be downloaded. For example, this will work for TXT or XLS files but will fail for F3D files.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object.```` ``` returnValue = dataFile_var.download(path, handler) ``` ```` |

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object.  ```` ``` #include <Core/Dashboard/DataFile.h>  returnValue = dataFile_var->download(path, handler); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns True in synchronous mode if successful. Returns True in asynchronous mode if the download was successfully started. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| path | string | The full path and optionally the filename used on the local file system for the file. If the path doesn't exist it will be created. If only a path is specified, the name and file extension associated with the DataFile is used for the filename. You can also specify the full path, including the filename. |
| handler | [DataEventHandler](DataEventHandler.htm) | If you want to do an asynchronous download, provide the handler object to be called when this operation is complete. To call the method synchronously, set this argument to null/None. |

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |