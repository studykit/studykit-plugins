# MFGDMDataEventArgs.firingEvent Property

Parent Object: [MFGDMDataEventArgs](MFGDMDataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MFGDMDataEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mFGDMDataEventArgs\_var" is a variable referencing a MFGDMDataEventArgs object. |

"mFGDMDataEventArgs\_var" is a variable referencing a MFGDMDataEventArgs object. ```` ``` #include <Core/Application/MFGDMDataEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = mFGDMDataEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |