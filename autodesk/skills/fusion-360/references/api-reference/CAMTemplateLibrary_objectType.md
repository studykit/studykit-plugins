# CAMTemplateLibrary.objectType Property

Parent Object: [CAMTemplateLibrary](CAMTemplateLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateLibrary.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateLibrary\_var" is a variable referencing a CAMTemplateLibrary object.  ```` ``` # Get the value of the property. propertyValue = cAMTemplateLibrary_var.objectType ``` ```` |

"cAMTemplateLibrary\_var" is a variable referencing a CAMTemplateLibrary object. ```` ``` #include <Cam/CAMTemplate/CAMTemplateLibrary.h>  // Get the value of the property. string propertyValue = cAMTemplateLibrary_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |