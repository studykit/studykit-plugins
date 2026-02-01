# ChamferFeatures.createInput Method

Parent Object: [ChamferFeatures](ChamferFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatures.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object.```` ``` returnValue = chamferFeatures_var.createInput(edges, isTangentChain) ``` ```` |

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object.  ```` ``` #include <Fusion/Features/ChamferFeatures.h>  returnValue = chamferFeatures_var->createInput(edges, isTangentChain); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ChamferFeatureInput](ChamferFeatureInput.htm) | Returns the newly created ChamferFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edges | [ObjectCollection](ObjectCollection.htm) | The collection of edges that will be chamfered. |
| isTangentChain | boolean | Boolean indicating if all edges that are tangentially connected to any of the input edges should be included in the chamfer or not. |

## Version

Introduced in version November 2014
Retired in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |