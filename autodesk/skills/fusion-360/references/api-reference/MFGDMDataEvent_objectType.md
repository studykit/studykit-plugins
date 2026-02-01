# MFGDMDataEvent.objectType Property

Parent Object: [MFGDMDataEvent](MFGDMDataEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MFGDMDataEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mFGDMDataEvent\_var" is a variable referencing a MFGDMDataEvent object.  ```` ``` # Get the value of the property. propertyValue = mFGDMDataEvent_var.objectType ``` ```` |

"mFGDMDataEvent\_var" is a variable referencing a MFGDMDataEvent object. ```` ``` #include <Core/Application/MFGDMDataEvent.h>  // Get the value of the property. string propertyValue = mFGDMDataEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |