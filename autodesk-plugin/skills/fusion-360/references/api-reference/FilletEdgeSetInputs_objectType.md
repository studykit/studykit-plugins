# FilletEdgeSetInputs.objectType Property

Parent Object: [FilletEdgeSetInputs](FilletEdgeSetInputs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSetInputs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSetInputs\_var" is a variable referencing a FilletEdgeSetInputs object.  ```` ``` # Get the value of the property. propertyValue = filletEdgeSetInputs_var.objectType ``` ```` |

"filletEdgeSetInputs\_var" is a variable referencing a FilletEdgeSetInputs object. ```` ``` #include <Fusion/Features/FilletEdgeSetInputs.h>  // Get the value of the property. string propertyValue = filletEdgeSetInputs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |