# MoveFeatures.objectType Property

Parent Object: [MoveFeatures](MoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatures\_var" is a variable referencing a MoveFeatures object.  ```` ``` # Get the value of the property. propertyValue = moveFeatures_var.objectType ``` ```` |

"moveFeatures\_var" is a variable referencing a MoveFeatures object. ```` ``` #include <Fusion/Features/MoveFeatures.h>  // Get the value of the property. string propertyValue = moveFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |