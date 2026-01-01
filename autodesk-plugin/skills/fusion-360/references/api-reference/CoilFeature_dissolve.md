# CoilFeature.dissolve Method

Parent Object: [CoilFeature](CoilFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeature\_var" is a variable referencing a [CoilFeature](CoilFeature.htm) object.```` ``` returnValue = coilFeature_var.dissolve() ``` ```` |

"coilFeature\_var" is a variable referencing a [CoilFeature](CoilFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |