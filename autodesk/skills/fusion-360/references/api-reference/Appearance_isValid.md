# Appearance.isValid Property

Parent Object: [Appearance](Appearance.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Appearance.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearance\_var" is a variable referencing an Appearance object. |

"appearance\_var" is a variable referencing an Appearance object. ```` ``` #include <Core/Materials/Appearance.h>  // Get the value of the property. boolean propertyValue = appearance_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |