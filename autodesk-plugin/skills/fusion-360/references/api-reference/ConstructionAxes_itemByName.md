# ConstructionAxes.itemByName Method

Parent Object: [ConstructionAxes](ConstructionAxes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxes.h>

## Description

Returns the specified construction axis using the name of the construction axis as it is displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxes\_var" is a variable referencing a [ConstructionAxes](ConstructionAxes.htm) object.```` ``` returnValue = constructionAxes_var.itemByName(name) ``` ```` |

"constructionAxes\_var" is a variable referencing a [ConstructionAxes](ConstructionAxes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionAxis](ConstructionAxis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the axis as it is displayed in the browser |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |