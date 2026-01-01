# CAMTemplateLibrary.childTemplates Method

Parent Object: [CAMTemplateLibrary](CAMTemplateLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateLibrary.h>

## Description

Get all templates by the given parent folder URL. Returns null if there is no folder at the URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object.```` ``` returnValue = cAMTemplateLibrary_var.childTemplates(url) ``` ```` |

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMTemplate](CAMTemplate.htm)[] | Returns an array of templates contained within the specified folder URL. Returns null if the URL is not valid. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL of the folder to get the templates from. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |