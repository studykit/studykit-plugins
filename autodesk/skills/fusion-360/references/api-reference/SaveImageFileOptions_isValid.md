# SaveImageFileOptions.isValid Property

Parent Object: [SaveImageFileOptions](SaveImageFileOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SaveImageFileOptions.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object. |

"saveImageFileOptions\_var" is a variable referencing a SaveImageFileOptions object. ```` ``` #include <Core/Application/SaveImageFileOptions.h>  // Get the value of the property. boolean propertyValue = saveImageFileOptions_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |