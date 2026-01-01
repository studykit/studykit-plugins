# CAMTemplateLibrary.templateAtURL Method

Parent Object: [CAMTemplateLibrary](CAMTemplateLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateLibrary.h>

## Description

Gets a specific template specified by the given URL. Returns null if the specified template does not exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object.```` ``` returnValue = cAMTemplateLibrary_var.templateAtURL(url) ``` ```` |

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMTemplate](CAMTemplate.htm) | Returns the template for a valid URL, returns null otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the template to be fetched. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |