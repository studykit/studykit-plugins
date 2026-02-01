# DataObject.saveToFile Method

Parent Object: [DataObject](DataObject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObject.h>

## Description

Saves the data represented by the DataObject to a file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataObject\_var" is a variable referencing a [DataObject](DataObject.htm) object.```` ``` returnValue = dataObject_var.saveToFile(filename) ``` ```` |

"dataObject\_var" is a variable referencing a [DataObject](DataObject.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the save was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The full filename to save the file to. This includes the full path and the filename. The folder must already exist and you are responsible for specifying the correct extension to match the file type. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |