# ShellFeature.dissolve Method

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a [ShellFeature](ShellFeature.htm) object.```` ``` returnValue = shellFeature_var.dissolve() ``` ```` |

"shellFeature\_var" is a variable referencing a [ShellFeature](ShellFeature.htm) object. |

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