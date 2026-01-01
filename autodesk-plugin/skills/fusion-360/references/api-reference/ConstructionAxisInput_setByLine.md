# ConstructionAxisInput.setByLine Method

Parent Object: [ConstructionAxisInput](ConstructionAxisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisInput.h>

## Description

This input method is for creating a non-parametric construction axis whose position in space is defined by an InfiniteLine3D object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisInput\_var" is a variable referencing a [ConstructionAxisInput](ConstructionAxisInput.htm) object.```` ``` returnValue = constructionAxisInput_var.setByLine(line) ``` ```` |

"constructionAxisInput\_var" is a variable referencing a [ConstructionAxisInput](ConstructionAxisInput.htm) object.  ```` ``` #include <Fusion/Construction/ConstructionAxisInput.h>  returnValue = constructionAxisInput_var->setByLine(line); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the creation of the ConstructionAxisInput is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [InfiniteLine3D](InfiniteLine3D.htm) | An InFiniteLine3D object |

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