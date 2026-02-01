# FlatPattern.isSuppressed Property

Parent Object: [FlatPattern](FlatPattern.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPattern.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPattern\_var" is a variable referencing a FlatPattern object. |

"flatPattern\_var" is a variable referencing a FlatPattern object. ```` ``` #include <Fusion/SheetMetal/FlatPattern.h>  // Get the value of the property. boolean propertyValue = flatPattern_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = flatPattern_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |