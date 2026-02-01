# Arrange3DDefinition.objectType Property

Parent Object: [Arrange3DDefinition](Arrange3DDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DDefinition\_var" is a variable referencing an Arrange3DDefinition object.  ```` ``` # Get the value of the property. propertyValue = arrange3DDefinition_var.objectType ``` ```` |

"arrange3DDefinition\_var" is a variable referencing an Arrange3DDefinition object. ```` ``` #include <Fusion/Arrange/Arrange3DDefinition.h>  // Get the value of the property. string propertyValue = arrange3DDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |