# CAMLibrary.createFolder Method

Parent Object: [CAMLibrary](CAMLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibrary.h>

## Description

Create a new folder in the library. Create the folder under given parent URL with given folder name. Add counting suffix, in case a folder with given name already exists. Throw an error if given URL does not point to a valid folder or the URL is read-only. Also throws an error if given folder name is empty.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibrary\_var" is a variable referencing a [CAMLibrary](CAMLibrary.htm) object.```` ``` returnValue = cAMLibrary_var.createFolder(parentUrl, folderName) ``` ```` |

"cAMLibrary\_var" is a variable referencing a [CAMLibrary](CAMLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL to the newly created folder |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parentUrl | [URL](URL.htm) | The parent URL for the folder to be created. |
| folderName | string | Name of the new folder to be created. Must not be empty. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |