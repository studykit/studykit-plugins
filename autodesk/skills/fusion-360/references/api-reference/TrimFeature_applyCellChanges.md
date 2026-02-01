# TrimFeature.applyCellChanges Method

Parent Object: [TrimFeature](TrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeature.h>

## Description

After making any changes to the set of selected cells you must call this method to indicate all changes have been made and to apply those changes to the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeature\_var" is a variable referencing a [TrimFeature](TrimFeature.htm) object.```` ``` returnValue = trimFeature_var.applyCellChanges() ``` ```` |

"trimFeature\_var" is a variable referencing a [TrimFeature](TrimFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the apply was successful. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |