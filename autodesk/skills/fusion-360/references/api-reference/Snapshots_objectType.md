# Snapshots.objectType Property

Parent Object: [Snapshots](Snapshots.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Snapshots.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"snapshots\_var" is a variable referencing a Snapshots object.  ```` ``` # Get the value of the property. propertyValue = snapshots_var.objectType ``` ```` |

"snapshots\_var" is a variable referencing a Snapshots object. ```` ``` #include <Fusion/Fusion/Snapshots.h>  // Get the value of the property. string propertyValue = snapshots_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |