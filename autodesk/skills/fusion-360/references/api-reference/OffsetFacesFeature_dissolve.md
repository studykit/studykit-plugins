# OffsetFacesFeature.dissolve Method

Parent Object: [OffsetFacesFeature](OffsetFacesFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeature\_var" is a variable referencing an [OffsetFacesFeature](OffsetFacesFeature.htm) object.```` ``` returnValue = offsetFacesFeature_var.dissolve() ``` ```` |

"offsetFacesFeature\_var" is a variable referencing an [OffsetFacesFeature](OffsetFacesFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |