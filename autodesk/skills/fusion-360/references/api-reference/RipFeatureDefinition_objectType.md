# RipFeatureDefinition.objectType Property

Parent Object: [RipFeatureDefinition](RipFeatureDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatureDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatureDefinition\_var" is a variable referencing a RipFeatureDefinition object.  ```` ``` # Get the value of the property. propertyValue = ripFeatureDefinition_var.objectType ``` ```` |

"ripFeatureDefinition\_var" is a variable referencing a RipFeatureDefinition object. ```` ``` #include <Fusion/SheetMetal/RipFeatureDefinition.h>  // Get the value of the property. string propertyValue = ripFeatureDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |