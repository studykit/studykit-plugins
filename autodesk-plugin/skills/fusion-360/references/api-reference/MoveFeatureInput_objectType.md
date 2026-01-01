# MoveFeatureInput.objectType Property

Parent Object: [MoveFeatureInput](MoveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureInput\_var" is a variable referencing a MoveFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = moveFeatureInput_var.objectType ``` ```` |

"moveFeatureInput\_var" is a variable referencing a MoveFeatureInput object. ```` ``` #include <Fusion/Features/MoveFeatureInput.h>  // Get the value of the property. string propertyValue = moveFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |