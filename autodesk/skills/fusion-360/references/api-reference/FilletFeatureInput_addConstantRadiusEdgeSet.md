# FilletFeatureInput.addConstantRadiusEdgeSet Method

Parent Object: [FilletFeatureInput](FilletFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method is obsolete. You should now use the methods on the EdgeSetInputs objects to define new fillets.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatureInput\_var" is a variable referencing a [FilletFeatureInput](FilletFeatureInput.htm) object.```` ``` returnValue = filletFeatureInput_var.addConstantRadiusEdgeSet(edges, radius, isTangentChain) ``` ```` |

"filletFeatureInput\_var" is a variable referencing a [FilletFeatureInput](FilletFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/FilletFeatureInput.h>  returnValue = filletFeatureInput_var->addConstantRadiusEdgeSet(edges, radius, isTangentChain); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the set of edges was successfully added to the FilletFeatureInput. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edges | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing the edges to be filleted. If the isTangentChain argument is true additional edges may also get filleted if they are tangentially connected to any of the input edges. |
| radius | [ValueInput](ValueInput.htm) | A ValueInput object that defines the radius of the fillet. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length. |
| isTangentChain | boolean | A boolean value for setting whether or not edges that are tangentially connected to the input edges (if any) will also be filleted. |

## Version

Introduced in version November 2014
Retired in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |