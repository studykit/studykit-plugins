# MFGDMDataEventArgs.objectType Property

Parent Object: [MFGDMDataEventArgs](MFGDMDataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MFGDMDataEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mFGDMDataEventArgs\_var" is a variable referencing a MFGDMDataEventArgs object.  ```` ``` # Get the value of the property. propertyValue = mFGDMDataEventArgs_var.objectType ``` ```` |

"mFGDMDataEventArgs\_var" is a variable referencing a MFGDMDataEventArgs object. ```` ``` #include <Core/Application/MFGDMDataEventArgs.h>  // Get the value of the property. string propertyValue = mFGDMDataEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |