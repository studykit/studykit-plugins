# ExtrudeFeature.dissolve Method

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object.```` ``` returnValue = extrudeFeature_var.dissolve() ``` ```` |

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |