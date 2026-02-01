# ConstructionPoints.itemByName Method

Parent Object: [ConstructionPoints](ConstructionPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoints.h>

## Description

Returns the specified construction point using the name of the construction point as it is displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoints\_var" is a variable referencing a [ConstructionPoints](ConstructionPoints.htm) object.```` ``` returnValue = constructionPoints_var.itemByName(name) ``` ```` |

"constructionPoints\_var" is a variable referencing a [ConstructionPoints](ConstructionPoints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionPoint](ConstructionPoint.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the construction point as it is displayed in the browser. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |