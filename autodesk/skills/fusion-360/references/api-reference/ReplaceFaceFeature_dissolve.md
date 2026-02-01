# ReplaceFaceFeature.dissolve Method

Parent Object: [ReplaceFaceFeature](ReplaceFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeature\_var" is a variable referencing a [ReplaceFaceFeature](ReplaceFaceFeature.htm) object.```` ``` returnValue = replaceFaceFeature_var.dissolve() ``` ```` |

"replaceFaceFeature\_var" is a variable referencing a [ReplaceFaceFeature](ReplaceFaceFeature.htm) object. |

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