# CAMTemplateLibrary.childFolderURLs Method

Parent Object: [CAMTemplateLibrary](CAMTemplateLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateLibrary.h>

## Description

Get all library folders under given URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object.```` ``` returnValue = cAMTemplateLibrary_var.childFolderURLs(url) ``` ```` |

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm)[] | Returns list of folder URLs at given location. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the parent folder. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |