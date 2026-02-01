# CAMLibrary.displayName Method

Parent Object: [CAMLibrary](CAMLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibrary.h>

## Description

Get the localized display name for a given URL. The URL must point to a folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibrary\_var" is a variable referencing a [CAMLibrary](CAMLibrary.htm) object.```` ``` returnValue = cAMLibrary_var.displayName(url) ``` ```` |

"cAMLibrary\_var" is a variable referencing a [CAMLibrary](CAMLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns localized display name for the folder. Returns empty string for invalid URL. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL that defines the path to a folder. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |