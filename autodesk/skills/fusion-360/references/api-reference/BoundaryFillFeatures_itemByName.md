# BoundaryFillFeatures.itemByName Method

Parent Object: [BoundaryFillFeatures](BoundaryFillFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatures.h>

## Description

Function that returns the specified boundary fill feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatures\_var" is a variable referencing a [BoundaryFillFeatures](BoundaryFillFeatures.htm) object.```` ``` returnValue = boundaryFillFeatures_var.itemByName(name) ``` ```` |

"boundaryFillFeatures\_var" is a variable referencing a [BoundaryFillFeatures](BoundaryFillFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoundaryFillFeature](BoundaryFillFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |