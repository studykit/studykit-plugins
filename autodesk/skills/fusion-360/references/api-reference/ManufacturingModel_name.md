# ManufacturingModel.name Property

Parent Object: [ManufacturingModel](ManufacturingModel.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModel.h>

## Description

Gets or sets the display name of the ManufacturingModel. This is the name that will be shown in the browser and other locations.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModel\_var" is a variable referencing a ManufacturingModel object. |

"manufacturingModel\_var" is a variable referencing a ManufacturingModel object. ```` ``` #include <Cam/ManufacturingModels/ManufacturingModel.h>  // Get the value of the property. string propertyValue = manufacturingModel_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = manufacturingModel_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |