# ConstructionAxes.createInput Method

Parent Object: [ConstructionAxes](ConstructionAxes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxes.h>

## Description

Create a ConstructionAxisInput object that is in turn used to create a ConstructionAxis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxes\_var" is a variable referencing a [ConstructionAxes](ConstructionAxes.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"constructionAxes\_var" is a variable referencing a [ConstructionAxes](ConstructionAxes.htm) object.  ```` ``` #include <Fusion/Construction/ConstructionAxes.h>  // Uses no optional arguments. returnValue = constructionAxes_var->createInput();  // Uses optional arguments. returnValue = constructionAxes_var->createInput(occurrenceForCreation); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionAxisInput](ConstructionAxisInput.htm) | Returns a ConstructionAxisInput object |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrenceForCreation | [Occurrence](Occurrence.htm) | A creation occurrence is needed if the input is in another component AND the construction axis is not in the root component. The occurrenceForCreation is analogous to the active occurrence in the UI.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Axis API Sample](ConstructionAxisSample_Sample.htm) | Demonstrates creating construction axis in various ways. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |