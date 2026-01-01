# ConstructionPlanes.itemByName Method

Parent Object: [ConstructionPlanes](ConstructionPlanes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlanes.h>

## Description

Returns the specified construction plane using the name of the construction plane as it is displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlanes\_var" is a variable referencing a [ConstructionPlanes](ConstructionPlanes.htm) object.```` ``` returnValue = constructionPlanes_var.itemByName(name) ``` ```` |

"constructionPlanes\_var" is a variable referencing a [ConstructionPlanes](ConstructionPlanes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionPlane](ConstructionPlane.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the construction plane as it is displayed in the browser |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |