# Feature.dissolve Method

Parent Object: [Feature](Feature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Feature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"feature\_var" is a variable referencing a [Feature](Feature.htm) object.```` ``` returnValue = feature_var.dissolve() ``` ```` |

"feature\_var" is a variable referencing a [Feature](Feature.htm) object. |

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