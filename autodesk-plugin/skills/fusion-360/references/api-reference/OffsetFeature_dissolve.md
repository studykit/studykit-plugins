# OffsetFeature.dissolve Method

Parent Object: [OffsetFeature](OffsetFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeature\_var" is a variable referencing an [OffsetFeature](OffsetFeature.htm) object.```` ``` returnValue = offsetFeature_var.dissolve() ``` ```` |

"offsetFeature\_var" is a variable referencing an [OffsetFeature](OffsetFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |