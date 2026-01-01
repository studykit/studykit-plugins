# CombineFeatures.createInput Method

Parent Object: [CombineFeatures](CombineFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatures.h>

## Description

Creates a CombineFeatureInput object. Use properties and methods on this object to define the combine you want to create and then use the Add method, passing in the CombineFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatures\_var" is a variable referencing a [CombineFeatures](CombineFeatures.htm) object.```` ``` returnValue = combineFeatures_var.createInput(targetBody, toolBodies) ``` ```` |

"combineFeatures\_var" is a variable referencing a [CombineFeatures](CombineFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CombineFeatureInput](CombineFeatureInput.htm) | Returns the newly created CombineFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targetBody | [BRepBody](BRepBody.htm) | A BRep body that represents the blank body. |
| toolBodies | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing one or more BRep bodies that represent tool bodies. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [combineFeatures.add](combineFeatures_add_Sample.htm) | Demonstrates the combineFeatures.add method. To use this sample, have a design open that contains at least two bodies. When you run the sample, you will be prompted to select the bodies and they will joined. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |