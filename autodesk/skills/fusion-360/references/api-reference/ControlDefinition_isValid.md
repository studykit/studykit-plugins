# ControlDefinition.isValid Property

Parent Object: [ControlDefinition](ControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ControlDefinition.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"controlDefinition\_var" is a variable referencing a ControlDefinition object. |

"controlDefinition\_var" is a variable referencing a ControlDefinition object. ```` ``` #include <Core/UserInterface/ControlDefinition.h>  // Get the value of the property. boolean propertyValue = controlDefinition_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |