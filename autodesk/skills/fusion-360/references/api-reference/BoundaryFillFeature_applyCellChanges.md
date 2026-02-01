# BoundaryFillFeature.applyCellChanges Method

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

After making any changes to the set of selected cells you must call this method to indicate all changes have been made and to apply those changes to the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a [BoundaryFillFeature](BoundaryFillFeature.htm) object.```` ``` returnValue = boundaryFillFeature_var.applyCellChanges() ``` ```` |

"boundaryFillFeature\_var" is a variable referencing a [BoundaryFillFeature](BoundaryFillFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the apply was successful. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |