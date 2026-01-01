# AlongPathTextDefinition.objectType Property

Parent Object: [AlongPathTextDefinition](AlongPathTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/AlongPathTextDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"alongPathTextDefinition\_var" is a variable referencing an AlongPathTextDefinition object.  ```` ``` # Get the value of the property. propertyValue = alongPathTextDefinition_var.objectType ``` ```` |

"alongPathTextDefinition\_var" is a variable referencing an AlongPathTextDefinition object. ```` ``` #include <Fusion/Sketch/AlongPathTextDefinition.h>  // Get the value of the property. string propertyValue = alongPathTextDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |