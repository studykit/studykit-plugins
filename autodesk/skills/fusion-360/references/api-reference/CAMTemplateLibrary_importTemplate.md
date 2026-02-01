# CAMTemplateLibrary.importTemplate Method

Parent Object: [CAMTemplateLibrary](CAMTemplateLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateLibrary.h>

## Description

Import a given template at a specific location. The template will be stored in the library. Throws an error if the given URL is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object.```` ``` returnValue = cAMTemplateLibrary_var.importTemplate(camTemplate, destinationUrl) ``` ```` |

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL of the newly imported template, or null if the import failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| camTemplate | [CAMTemplate](CAMTemplate.htm) | The template that should be imported. |
| destinationUrl | [URL](URL.htm) | The URL to the folder where to save the template. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |