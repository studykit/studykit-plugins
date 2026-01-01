# DataFolder.uploadFile Method

Parent Object: [DataFolder](DataFolder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolder.h>

## Description

Uploads a single file to this directory.

## Remarks

Uploading a file is not supported within any of the Command related events. When a command is running, a transaction is open, and uploading files cannot be transacted and, as a result, cannot be contained within a command transaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolder\_var" is a variable referencing a [DataFolder](DataFolder.htm) object.```` ``` returnValue = dataFolder_var.uploadFile(filename) ``` ```` |

"dataFolder\_var" is a variable referencing a [DataFolder](DataFolder.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFileFuture](DataFileFuture.htm) | The upload process is asynchronous which means that this method will return before the upload process had completed. The returned DataFileFuture object can be used to check on the current state of the upload to determine if it is still uploading, is complete, or has failed. If it is complete the final DataFinal can be retrieved through the DataFileFuture object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The full filename of the file to upload. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |