# CylinderFeature.dissolve Method

Parent Object: [CylinderFeature](CylinderFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CylinderFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinderFeature\_var" is a variable referencing a [CylinderFeature](CylinderFeature.htm) object.```` ``` returnValue = cylinderFeature_var.dissolve() ``` ```` |

"cylinderFeature\_var" is a variable referencing a [CylinderFeature](CylinderFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |