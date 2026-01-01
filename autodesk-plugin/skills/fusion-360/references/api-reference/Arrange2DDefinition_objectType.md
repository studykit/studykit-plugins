# Arrange2DDefinition.objectType Property

Parent Object: [Arrange2DDefinition](Arrange2DDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object.  ```` ``` # Get the value of the property. propertyValue = arrange2DDefinition_var.objectType ``` ```` |

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. ```` ``` #include <Fusion/Arrange/Arrange2DDefinition.h>  // Get the value of the property. string propertyValue = arrange2DDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |