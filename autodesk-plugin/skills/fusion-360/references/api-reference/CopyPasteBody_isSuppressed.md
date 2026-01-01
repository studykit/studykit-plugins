# CopyPasteBody.isSuppressed Property

Parent Object: [CopyPasteBody](CopyPasteBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBody.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyPasteBody\_var" is a variable referencing a CopyPasteBody object. |

"copyPasteBody\_var" is a variable referencing a CopyPasteBody object. ```` ``` #include <Fusion/Features/CopyPasteBody.h>  // Get the value of the property. boolean propertyValue = copyPasteBody_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = copyPasteBody_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |