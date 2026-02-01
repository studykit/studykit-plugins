# ManufacturingModel.objectType Property

Parent Object: [ManufacturingModel](ManufacturingModel.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModel.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModel\_var" is a variable referencing a ManufacturingModel object.  ```` ``` # Get the value of the property. propertyValue = manufacturingModel_var.objectType ``` ```` |

"manufacturingModel\_var" is a variable referencing a ManufacturingModel object. ```` ``` #include <Cam/ManufacturingModels/ManufacturingModel.h>  // Get the value of the property. string propertyValue = manufacturingModel_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |