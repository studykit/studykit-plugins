# SplitBodyFeature.dissolve Method

Parent Object: [SplitBodyFeature](SplitBodyFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeature\_var" is a variable referencing a [SplitBodyFeature](SplitBodyFeature.htm) object.```` ``` returnValue = splitBodyFeature_var.dissolve() ``` ```` |

"splitBodyFeature\_var" is a variable referencing a [SplitBodyFeature](SplitBodyFeature.htm) object. |

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