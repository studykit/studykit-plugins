# MoveFeature.isSuppressed Property

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a MoveFeature object. |

"moveFeature\_var" is a variable referencing a MoveFeature object. ```` ``` #include <Fusion/Features/MoveFeature.h>  // Get the value of the property. boolean propertyValue = moveFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = moveFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |