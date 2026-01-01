# CAMFolder.isSuppressed Property

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

Gets and sets the "Suppressed" property value of the operation. Gets/sets true if the operation is suppressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a CAMFolder object. |

"cAMFolder\_var" is a variable referencing a CAMFolder object. ```` ``` #include <Cam/CAM/CAMFolder.h>  // Get the value of the property. boolean propertyValue = cAMFolder_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = cAMFolder_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |