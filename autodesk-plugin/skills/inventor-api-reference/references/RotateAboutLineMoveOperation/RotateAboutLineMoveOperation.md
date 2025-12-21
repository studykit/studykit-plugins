# RotateAboutLineMoveOperation Object

Derived from: [MoveOperation](../MoveOperation/MoveOperation.md) Object

## Description

The RotateAboutLineMoveOperation object represents the definition of a rotation about a line within a move feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation_Delete.md) | Method that deletes this operation from the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Angle](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation_Angle.md) | Read-write property that provides access to the angle of a rotate about line operation on a move body feature. |
| [Application](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AxisEntity](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation_AxisEntity.md) | Read-write property that gets and sets the entity used to define the axis or rotation. |
| [Parent](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation_Parent.md) | Read-only property returning the associated MoveDefinition object. |
| [Type](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEntityNaturalDirection](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation_UseEntityNaturalDirection.md) | Read-write Boolean property that specifies if the rotation direction of the bodies uses the natural direction of the direction entity. |

## Accessed From

[MoveDefinition.AddRotateAboutAxis](../MoveDefinition/MoveDefinition_AddRotateAboutAxis.md)

## Version

Introduced in version 2013
