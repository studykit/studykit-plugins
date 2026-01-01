# Palettes.isValid Property

Parent Object: [Palettes](Palettes.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palettes.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palettes\_var" is a variable referencing a Palettes object. |

"palettes\_var" is a variable referencing a Palettes object. ```` ``` #include <Core/UserInterface/Palettes.h>  // Get the value of the property. boolean propertyValue = palettes_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |