# ManufacturingModels.syncAllManufacturingModels Method

Parent Object: [ManufacturingModels](ManufacturingModels.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModels.h>

## Description

Checks wether changes to the original design have been made. If so, all manufacturing models are synchronized with their sources.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModels\_var" is a variable referencing a [ManufacturingModels](ManufacturingModels.htm) object.```` ``` returnValue = manufacturingModels_var.syncAllManufacturingModels() ``` ```` |

"manufacturingModels\_var" is a variable referencing a [ManufacturingModels](ManufacturingModels.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if any manufacturing model needed an update. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |