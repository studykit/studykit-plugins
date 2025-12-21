# MoveOperation Object

## Description

The MoveOperation object is the base class for the various type of move operations that can be defined for a move body feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MoveOperation/MoveOperation_Delete.md) | Method that deletes this operation from the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MoveOperation/MoveOperation_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../MoveOperation/MoveOperation_Parent.md) | Read-only property returning the associated MoveDefinition object. |
| [Type](../MoveOperation/MoveOperation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[MoveDefinition.MoveOperation](../MoveDefinition/MoveDefinition_MoveOperation.md)

## Derived Classes

[FreeDragMoveOperation](../FreeDragMoveOperation/FreeDragMoveOperation.md), [MoveAlongRayMoveOperation](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation.md), [RotateAboutLineMoveOperation](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation.md)

## Version

Introduced in version 2013
