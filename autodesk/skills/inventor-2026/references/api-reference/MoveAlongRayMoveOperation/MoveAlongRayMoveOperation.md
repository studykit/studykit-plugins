# MoveAlongRayMoveOperation Object

Derived from: [MoveOperation](../MoveOperation/MoveOperation.md) Object

## Description

The MoveAlongRayMoveOperation object represents the definition of a move along a specified direction within a move feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation_Delete.md) | Method that deletes this operation from the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DirectionEntity](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation_DirectionEntity.md) | Read-write property that gets and sets the entity used to define the direction of the move. |
| [EntityNaturalDirection](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation_EntityNaturalDirection.md) | Read-write Boolean property that specifies if the movement direction of the bodies is in the natural direction of the direction entity. |
| [Offset](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation_Offset.md) | Read-write property that provides access to the offset of a move along ray operation on a move body feature. |
| [Parent](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation_Parent.md) | Read-only property returning the associated MoveDefinition object. |
| [Type](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[MoveDefinition.AddMoveAlongRay](../MoveDefinition/MoveDefinition_AddMoveAlongRay.md)

## Version

Introduced in version 2013
