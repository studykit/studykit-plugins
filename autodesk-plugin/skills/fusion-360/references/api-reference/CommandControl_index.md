# CommandControl.index Property

Parent Object: [CommandControl](CommandControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandControl.h>

## Description

Gets the position of this control within the list of controls within the panel, toolbar, or drop-down control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandControl\_var" is a variable referencing a CommandControl object. |

"commandControl\_var" is a variable referencing a CommandControl object. ```` ``` #include <Core/UserInterface/CommandControl.h>  // Get the value of the property. uinteger propertyValue = commandControl_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |