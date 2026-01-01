# ReverseNormalFeature.dissolve Method

Parent Object: [ReverseNormalFeature](ReverseNormalFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeature\_var" is a variable referencing a [ReverseNormalFeature](ReverseNormalFeature.htm) object.```` ``` returnValue = reverseNormalFeature_var.dissolve() ``` ```` |

"reverseNormalFeature\_var" is a variable referencing a [ReverseNormalFeature](ReverseNormalFeature.htm) object. |

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