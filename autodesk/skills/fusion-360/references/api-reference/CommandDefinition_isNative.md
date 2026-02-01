# CommandDefinition.isNative Property

Parent Object: [CommandDefinition](CommandDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinition.h>

## Description

Gets if this is a native command definition. If True then there are limitations to edits that can be done on the command definition. For example a native command definition cannot be deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinition\_var" is a variable referencing a CommandDefinition object. |

"commandDefinition\_var" is a variable referencing a CommandDefinition object. ```` ``` #include <Core/UserInterface/CommandDefinition.h>  // Get the value of the property. boolean propertyValue = commandDefinition_var->isNative(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |