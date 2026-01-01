# MoveFeatures.add Method

Parent Object: [MoveFeatures](MoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatures.h>

## Description

Creates a new move feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object.```` ``` returnValue = moveFeatures_var.add(input) ``` ```` |

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MoveFeature](MoveFeature.htm) | Returns the newly created MoveFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MoveFeatureInput](MoveFeatureInput.htm) | A MoveFeatureInput object that defines the desired move feature. Use the createInput2 method to create a new MoveFeatureInput object and then use methods on the MoveFeatureInput object to define the move feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [moveFeatures.add](moveFeatures_add_Sample.htm) | Demonstrates the moveFeatures.add method. |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |