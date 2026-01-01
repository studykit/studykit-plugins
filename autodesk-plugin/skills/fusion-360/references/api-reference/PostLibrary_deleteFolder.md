# PostLibrary.deleteFolder Method

Parent Object: [PostLibrary](PostLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostLibrary.h>

## Description

Delete folder by URL from the library. Any content of the folder will also be deleted. Throw an error if given URL does not point to a valid folder or the URL is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postLibrary\_var" is a variable referencing a [PostLibrary](PostLibrary.htm) object.```` ``` returnValue = postLibrary_var.deleteFolder(url) ``` ```` |

"postLibrary\_var" is a variable referencing a [PostLibrary](PostLibrary.htm) object. |

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