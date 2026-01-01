# ConstructionPoints.createInput Method

Parent Object: [ConstructionPoints](ConstructionPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoints.h>

## Description

Create a ConstructionPointInput object that is in turn used to create a ConstructionPoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoints\_var" is a variable referencing a [ConstructionPoints](ConstructionPoints.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"constructionPoints\_var" is a variable referencing a [ConstructionPoints](ConstructionPoints.htm) object.  ```` ``` #include <Fusion/Construction/ConstructionPoints.h>  // Uses no optional arguments. returnValue = constructionPoints_var->createInput();  // Uses optional arguments. returnValue = constructionPoints_var->createInput(occurrenceForCreation); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionPointInput](ConstructionPointInput.htm) | Returns a ConstructionPointInput object |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrenceForCreation | [Occurrence](Occurrence.htm) | A creation occurrence is needed if the input is in another component AND the construction point is not in the root component. The occurrenceForCreation is analogous to the active occurrence in the UI.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Point API Sample](ConstructionPointSample_Sample.htm) | Demonstrates creating construction point by different ways |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |