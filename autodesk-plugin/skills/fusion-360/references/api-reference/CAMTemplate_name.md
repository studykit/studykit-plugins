# CAMTemplate.name Property

Parent Object: [CAMTemplate](CAMTemplate.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplate.h>

## Description

Gets and sets the name of the template.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplate\_var" is a variable referencing a CAMTemplate object. |

"cAMTemplate\_var" is a variable referencing a CAMTemplate object. ```` ``` #include <Cam/CAMTemplate/CAMTemplate.h>  // Get the value of the property. string propertyValue = cAMTemplate_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = cAMTemplate_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |