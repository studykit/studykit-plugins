# ManufacturingModelInput.objectType Property

Parent Object: [ManufacturingModelInput](ManufacturingModelInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModelInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModelInput\_var" is a variable referencing a ManufacturingModelInput object.  ```` ``` # Get the value of the property. propertyValue = manufacturingModelInput_var.objectType ``` ```` |

"manufacturingModelInput\_var" is a variable referencing a ManufacturingModelInput object. ```` ``` #include <Cam/ManufacturingModels/ManufacturingModelInput.h>  // Get the value of the property. string propertyValue = manufacturingModelInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |