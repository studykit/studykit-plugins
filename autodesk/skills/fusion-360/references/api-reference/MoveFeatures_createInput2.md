# MoveFeatures.createInput2 Method

Parent Object: [MoveFeatures](MoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatures.h>

## Description

Creates a MoveFeatureInput object. Use properties and methods on this object to define how the move is defined and then use the MoveFeatues.add method, passing in the MoveFeatureInput object to create a move feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object.```` ``` returnValue = moveFeatures_var.createInput2(inputEntities) ``` ```` |

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MoveFeatureInput](MoveFeatureInput.htm) | Returns the newly created MoveFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEntities | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing the objects to move. For a parametric model, the collection can contain BRepBody or BRepFace objects but not a combination of both. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [moveFeatures.add](moveFeatures_add_Sample.htm) | Demonstrates the moveFeatures.add method. |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |