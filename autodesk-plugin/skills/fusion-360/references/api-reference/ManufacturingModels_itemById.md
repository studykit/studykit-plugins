# ManufacturingModels.itemById Method

Parent Object: [ManufacturingModels](ManufacturingModels.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModels.h>

## Description

Returns ManufacturingModel with given id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModels\_var" is a variable referencing a [ManufacturingModels](ManufacturingModels.htm) object.```` ``` returnValue = manufacturingModels_var.itemById(id) ``` ```` |

"manufacturingModels\_var" is a variable referencing a [ManufacturingModels](ManufacturingModels.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ManufacturingModel](ManufacturingModel.htm) | Returns ManufacturingModel with the specified id or null if no ManufacturingModel has that id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The id of the ManufacturingModel. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |