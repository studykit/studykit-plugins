# ConstructionPlanes.createInput Method

Parent Object: [ConstructionPlanes](ConstructionPlanes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlanes.h>

## Description

Create a ConstructionPlaneInput object that is in turn used to create a ConstructionPlane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlanes\_var" is a variable referencing a [ConstructionPlanes](ConstructionPlanes.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"constructionPlanes\_var" is a variable referencing a [ConstructionPlanes](ConstructionPlanes.htm) object.  ```` ``` #include <Fusion/Construction/ConstructionPlanes.h>  // Uses no optional arguments. returnValue = constructionPlanes_var->createInput();  // Uses optional arguments. returnValue = constructionPlanes_var->createInput(occurrenceForCreation); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionPlaneInput](ConstructionPlaneInput.htm) | Returns a ConstructionPlaneInput object |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrenceForCreation | [Occurrence](Occurrence.htm) | A creation occurrence is needed if the input is in another component AND the construction plane is not in the root component. The occurrenceForCreation is analogous to the active occurrence in the UI.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Plane API Sample](ConstructionPlaneSample_Sample.htm) | Demonstrates creating construction plane by different ways. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |