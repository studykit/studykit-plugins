# ModifyUtility.isValid Property

Parent Object: [ModifyUtility](ModifyUtility.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ModifyUtility/ModifyUtility.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modifyUtility\_var" is a variable referencing a ModifyUtility object. |

"modifyUtility\_var" is a variable referencing a ModifyUtility object. ```` ``` #include <Cam/ModifyUtility/ModifyUtility.h>  // Get the value of the property. boolean propertyValue = modifyUtility_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |