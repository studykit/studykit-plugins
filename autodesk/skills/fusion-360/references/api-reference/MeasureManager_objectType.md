# MeasureManager.objectType Property

Parent Object: [MeasureManager](MeasureManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MeasureManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"measureManager\_var" is a variable referencing a MeasureManager object.  ```` ``` # Get the value of the property. propertyValue = measureManager_var.objectType ``` ```` |

"measureManager\_var" is a variable referencing a MeasureManager object. ```` ``` #include <Core/Application/MeasureManager.h>  // Get the value of the property. string propertyValue = measureManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |