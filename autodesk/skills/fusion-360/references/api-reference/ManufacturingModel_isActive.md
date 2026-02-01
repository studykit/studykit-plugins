# ManufacturingModel.isActive Property

Parent Object: [ManufacturingModel](ManufacturingModel.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModel.h>

## Description

Gets whether this ManufacturingModel is active in the user interface. This is the same as checking the state of the radio button next to the ManufacturingModel in the browser. To activate the ManufacturingModel use the Activate method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModel\_var" is a variable referencing a ManufacturingModel object. |

"manufacturingModel\_var" is a variable referencing a ManufacturingModel object. ```` ``` #include <Cam/ManufacturingModels/ManufacturingModel.h>  // Get the value of the property. boolean propertyValue = manufacturingModel_var->isActive(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |