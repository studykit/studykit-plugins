# CommandDefinition.isValid Property

Parent Object: [CommandDefinition](CommandDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinition.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinition\_var" is a variable referencing a CommandDefinition object. |

"commandDefinition\_var" is a variable referencing a CommandDefinition object. ```` ``` #include <Core/UserInterface/CommandDefinition.h>  // Get the value of the property. boolean propertyValue = commandDefinition_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |