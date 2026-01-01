# MoveFeatures.isValid Property

Parent Object: [MoveFeatures](MoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatures\_var" is a variable referencing a MoveFeatures object. |

"moveFeatures\_var" is a variable referencing a MoveFeatures object. ```` ``` #include <Fusion/Features/MoveFeatures.h>  // Get the value of the property. boolean propertyValue = moveFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |