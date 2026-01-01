# DataFile.refresh Method

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Refreshes the data associated with a DataFile object to be up to date with the associated cloud data. The DataFile returned by the API reflects the local representation of the DataFile as used by the Data Panel. This is method is only useful in very limited cases and should rarely be used. In most cases the local representation will match the actual data on the cloud. In rare occasions where Fusion was off-line while the cloud processing of DataFile is completed or the DataFile is not in the folder shown in the Data Panel. Getting a DataFileFolder contents forces an update of the local data for all of the data files it contains so they will all be up to date.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object.```` ``` returnValue = dataFile_var.refresh(handler) ``` ```` |

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns True in synchronous mode if successful. Returns True in asynchronous mode if the refresh was successfully started. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [DataEventHandler](DataEventHandler.htm) | If you want to do an asynchronous refresh, provide the handler object to be called when this operation is complete. To call the method synchronously, set this argument to null/None. |

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |