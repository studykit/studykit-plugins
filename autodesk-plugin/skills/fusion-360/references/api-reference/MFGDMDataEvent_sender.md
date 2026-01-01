# MFGDMDataEvent.sender Property

Parent Object: [MFGDMDataEvent](MFGDMDataEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MFGDMDataEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mFGDMDataEvent\_var" is a variable referencing a MFGDMDataEvent object. |

"mFGDMDataEvent\_var" is a variable referencing a MFGDMDataEvent object. ```` ``` #include <Core/Application/MFGDMDataEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = mFGDMDataEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |