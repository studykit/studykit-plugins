# Material.copyTo Method

Parent Object: [Material](Material.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Material.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been retired and replaced by the addByCopyMethod on the Materials object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"material\_var" is a variable referencing a [Material](Material.htm) object.```` ``` returnValue = material_var.copyTo(target) ``` ```` |

"material\_var" is a variable referencing a [Material](Material.htm) object.  ```` ``` #include <Core/Materials/Material.h>  returnValue = material_var->copyTo(target); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Material](Material.htm) | Returns the new copy of the material or null if the copy failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| target | [Base](Base.htm) | The target can be a Design or MaterialFavorites object. |

## Version

Introduced in version August 2014
Retired in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |