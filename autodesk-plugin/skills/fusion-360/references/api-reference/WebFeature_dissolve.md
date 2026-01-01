# WebFeature.dissolve Method

Parent Object: [WebFeature](WebFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/WebFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webFeature\_var" is a variable referencing a [WebFeature](WebFeature.htm) object.```` ``` returnValue = webFeature_var.dissolve() ``` ```` |

"webFeature\_var" is a variable referencing a [WebFeature](WebFeature.htm) object. |

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