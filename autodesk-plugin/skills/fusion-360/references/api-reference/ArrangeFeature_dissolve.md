# ArrangeFeature.dissolve Method

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an [ArrangeFeature](ArrangeFeature.htm) object.```` ``` returnValue = arrangeFeature_var.dissolve() ``` ```` |

"arrangeFeature\_var" is a variable referencing an [ArrangeFeature](ArrangeFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |