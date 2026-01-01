# SilhouetteSplitFeature.dissolve Method

Parent Object: [SilhouetteSplitFeature](SilhouetteSplitFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeature\_var" is a variable referencing a [SilhouetteSplitFeature](SilhouetteSplitFeature.htm) object.```` ``` returnValue = silhouetteSplitFeature_var.dissolve() ``` ```` |

"silhouetteSplitFeature\_var" is a variable referencing a [SilhouetteSplitFeature](SilhouetteSplitFeature.htm) object. |

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