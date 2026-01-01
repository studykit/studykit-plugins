# ManufacturingModel.isValid Property

Parent Object: [ManufacturingModel](ManufacturingModel.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModel.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModel\_var" is a variable referencing a ManufacturingModel object. |

"manufacturingModel\_var" is a variable referencing a ManufacturingModel object. ```` ``` #include <Cam/ManufacturingModels/ManufacturingModel.h>  // Get the value of the property. boolean propertyValue = manufacturingModel_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |