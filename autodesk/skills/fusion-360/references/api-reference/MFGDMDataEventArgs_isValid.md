# MFGDMDataEventArgs.isValid Property

Parent Object: [MFGDMDataEventArgs](MFGDMDataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MFGDMDataEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mFGDMDataEventArgs\_var" is a variable referencing a MFGDMDataEventArgs object. |

"mFGDMDataEventArgs\_var" is a variable referencing a MFGDMDataEventArgs object. ```` ``` #include <Core/Application/MFGDMDataEventArgs.h>  // Get the value of the property. boolean propertyValue = mFGDMDataEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |