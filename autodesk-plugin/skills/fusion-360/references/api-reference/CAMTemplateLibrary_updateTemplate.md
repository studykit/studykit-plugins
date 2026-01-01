# CAMTemplateLibrary.updateTemplate Method

Parent Object: [CAMTemplateLibrary](CAMTemplateLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateLibrary.h>

## Description

Update a template in the library. The library substitutes the existing template at the URL by given template. Throws an error if the URL does not already point to an existing template. If the name member of the CAMTemplate doesn't match the name portion of the URL then this will include a rename operation and the returned URL will reflect the new name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object.```` ``` returnValue = cAMTemplateLibrary_var.updateTemplate(camTemplate, url) ``` ```` |

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL of the updated template, or null if the update failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| camTemplate | [CAMTemplate](CAMTemplate.htm) | The template that should be persisted. |
| url | [URL](URL.htm) | The URL to the existing template in the library that should be updated. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |