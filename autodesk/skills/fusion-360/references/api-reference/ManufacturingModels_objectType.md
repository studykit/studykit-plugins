# ManufacturingModels.objectType Property

Parent Object: [ManufacturingModels](ManufacturingModels.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModels.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModels\_var" is a variable referencing a ManufacturingModels object.  ```` ``` # Get the value of the property. propertyValue = manufacturingModels_var.objectType ``` ```` |

"manufacturingModels\_var" is a variable referencing a ManufacturingModels object. ```` ``` #include <Cam/ManufacturingModels/ManufacturingModels.h>  // Get the value of the property. string propertyValue = manufacturingModels_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |