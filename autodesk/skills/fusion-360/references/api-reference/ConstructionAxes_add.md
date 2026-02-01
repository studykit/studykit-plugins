# ConstructionAxes.add Method

Parent Object: [ConstructionAxes](ConstructionAxes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxes.h>

## Description

Creates and adds a new ConstructionAxis using the creation parameters in the ConstructionAxisInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxes\_var" is a variable referencing a [ConstructionAxes](ConstructionAxes.htm) object.```` ``` returnValue = constructionAxes_var.add(input) ``` ```` |

"constructionAxes\_var" is a variable referencing a [ConstructionAxes](ConstructionAxes.htm) object.  ```` ``` #include <Fusion/Construction/ConstructionAxes.h>  returnValue = constructionAxes_var->add(input); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionAxis](ConstructionAxis.htm) | Returns the newly created construction axis or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ConstructionAxisInput](ConstructionAxisInput.htm) | A ConstructionAxisInput object |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Axis API Sample](ConstructionAxisSample_Sample.htm) | Demonstrates creating construction axis in various ways. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |