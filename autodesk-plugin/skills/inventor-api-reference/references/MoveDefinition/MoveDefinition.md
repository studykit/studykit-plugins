# MoveDefinition Object

## Description

The MoveDefinition object is used to define all of the input required for move body features. It is also used to query and edit existing move body features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddFreeDrag](../MoveDefinition/MoveDefinition_AddFreeDrag.md) | Method that creates a free drag operation on the associated move body feature. |
| [AddMoveAlongRay](../MoveDefinition/MoveDefinition_AddMoveAlongRay.md) | Method that creates a move along ray operation on the associated move body feature. |
| [AddRotateAboutAxis](../MoveDefinition/MoveDefinition_AddRotateAboutAxis.md) | Method that creates a move rotate about azis operation on the associated move body feature. |
| [Copy](../MoveDefinition/MoveDefinition_Copy.md) | Method that returns a copy of the MoveDefinition object. The copy is independent of any feature and making edits to it will not change any feature. A common workflow if you need to makes several edits to a feature is to copy the definition, makes the changes and then assign the definition back to the feature so that all of the edits are made as part of a single update. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MoveDefinition/MoveDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [MoveOperation](../MoveDefinition/MoveDefinition_MoveOperation.md) | Property that returns the specified MoveOperation object. They are returned in the same order that they were applied. The MoveOperationCount property can used to determine the number of operations avaialable. |
| [MoveOperationCount](../MoveDefinition/MoveDefinition_MoveOperationCount.md) | Property that returns the number of move operations associated with this definition. The MoveOperation property can be used to access a specific operation. |
| [Parent](../MoveDefinition/MoveDefinition_Parent.md) | Read-only property that returns the parent MoveFeature of the definition. This can return Nothing in the case where this definition is transient and is not associated with any feature. |
| [SurfaceBodies](../MoveDefinition/MoveDefinition_SurfaceBodies.md) | Read-write property that gets and sets the set of bodies that are affected by this feature. |
| [Type](../MoveDefinition/MoveDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FreeDragMoveOperation.Parent](../FreeDragMoveOperation/FreeDragMoveOperation_Parent.md), [MoveAlongRayMoveOperation.Parent](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation_Parent.md), [MoveDefinition.Copy](../MoveDefinition/MoveDefinition_Copy.md), [MoveFeature.Definition](../MoveFeature/MoveFeature_Definition.md), [MoveFeatureProxy.Definition](../MoveFeatureProxy/MoveFeatureProxy_Definition.md), [MoveFeatures.CreateMoveDefinition](../MoveFeatures/MoveFeatures_CreateMoveDefinition.md), [MoveOperation.Parent](../MoveOperation/MoveOperation_Parent.md), [RotateAboutLineMoveOperation.Parent](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Move Feature Creation](../../sample-programs/MoveBodyFeatures_Sample.md) | Demonstrates the creation of a Move feature. |

## Version

Introduced in version 2013
