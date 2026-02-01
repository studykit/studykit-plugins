# FreeDragMoveOperation Object

Derived from: [MoveOperation](../MoveOperation/MoveOperation.md) Object

## Description

The FreeDragMoveOperation object represents the definition of a free drag within a move feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FreeDragMoveOperation/FreeDragMoveOperation_Delete.md) | Method that deletes this operation from the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FreeDragMoveOperation/FreeDragMoveOperation_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../FreeDragMoveOperation/FreeDragMoveOperation_Parent.md) | Read-only property returning the associated MoveDefinition object. |
| [Type](../FreeDragMoveOperation/FreeDragMoveOperation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [XOffset](../FreeDragMoveOperation/FreeDragMoveOperation_XOffset.md) | Read-write property that provides access to the x offset of a free drag operation on a move body feature. |
| [YOffset](../FreeDragMoveOperation/FreeDragMoveOperation_YOffset.md) | Read-write property that provides access to the y offset of a free drag operation on a move body feature. |
| [ZOffset](../FreeDragMoveOperation/FreeDragMoveOperation_ZOffset.md) | Read-write property that provides access to the z offset of a free drag operation on a move body feature. |

## Accessed From

[MoveDefinition.AddFreeDrag](../MoveDefinition/MoveDefinition_AddFreeDrag.md)

## Version

Introduced in version 2013
