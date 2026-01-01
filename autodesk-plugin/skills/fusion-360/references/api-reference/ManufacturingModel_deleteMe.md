# ManufacturingModel.deleteMe Method

Parent Object: [ManufacturingModel](ManufacturingModel.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModel.h>

## Description

Deletes this ManufacturingModel. If this is part of a setup, the reference to this will be lost. The deletion makes that reference invalid.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModel\_var" is a variable referencing a [ManufacturingModel](ManufacturingModel.htm) object.```` ``` returnValue = manufacturingModel_var.deleteMe() ``` ```` |

"manufacturingModel\_var" is a variable referencing a [ManufacturingModel](ManufacturingModel.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete is successful. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |