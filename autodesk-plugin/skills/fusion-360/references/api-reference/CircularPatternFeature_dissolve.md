# CircularPatternFeature.dissolve Method

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a [CircularPatternFeature](CircularPatternFeature.htm) object.```` ``` returnValue = circularPatternFeature_var.dissolve() ``` ```` |

"circularPatternFeature\_var" is a variable referencing a [CircularPatternFeature](CircularPatternFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |