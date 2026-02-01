# MultiLineTextDefinition.objectType Property

Parent Object: [MultiLineTextDefinition](MultiLineTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MultiLineTextDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiLineTextDefinition\_var" is a variable referencing a MultiLineTextDefinition object.  ```` ``` # Get the value of the property. propertyValue = multiLineTextDefinition_var.objectType ``` ```` |

"multiLineTextDefinition\_var" is a variable referencing a MultiLineTextDefinition object. ```` ``` #include <Fusion/Sketch/MultiLineTextDefinition.h>  // Get the value of the property. string propertyValue = multiLineTextDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |