# ManufacturingModels.itemByName Method

Parent Object: [ManufacturingModels](ManufacturingModels.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModels.h>

## Description

Returns all ManufacturingModel with given name (as appears in the browser).

## Syntax

* [Python](#Python)
* [C++](#C++)

"manufacturingModels\_var" is a variable referencing a [ManufacturingModels](ManufacturingModels.htm) object.```` ``` returnValue = manufacturingModels_var.itemByName(name) ``` ```` |

"manufacturingModels\_var" is a variable referencing a [ManufacturingModels](ManufacturingModels.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ManufacturingModel](ManufacturingModel.htm)[] | Returns all ManufacturingModel with the specified name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name (as it appears in the browser) of the ManufacturingModel. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |