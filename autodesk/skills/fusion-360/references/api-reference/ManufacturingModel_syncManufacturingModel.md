# ManufacturingModel.syncManufacturingModel Method

Parent Object: [ManufacturingModel](ManufacturingModel.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModel.h>

## Description

Checks whether changes to the original design have been made. If so, the given manufacturing model is synchronized with its source.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModel\_var" is a variable referencing a [ManufacturingModel](ManufacturingModel.htm) object.```` ``` returnValue = manufacturingModel_var.syncManufacturingModel() ``` ```` |

"manufacturingModel\_var" is a variable referencing a [ManufacturingModel](ManufacturingModel.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the manufacturing model needed an update. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |