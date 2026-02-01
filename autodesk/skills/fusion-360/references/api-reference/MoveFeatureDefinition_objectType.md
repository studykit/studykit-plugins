# MoveFeatureDefinition.objectType Property

Parent Object: [MoveFeatureDefinition](MoveFeatureDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureDefinition\_var" is a variable referencing a MoveFeatureDefinition object.  ```` ``` # Get the value of the property. propertyValue = moveFeatureDefinition_var.objectType ``` ```` |

"moveFeatureDefinition\_var" is a variable referencing a MoveFeatureDefinition object. ```` ``` #include <Fusion/Features/MoveFeatureDefinition.h>  // Get the value of the property. string propertyValue = moveFeatureDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |