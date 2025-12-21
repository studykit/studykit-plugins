# FlatBendResult Object

## Description

The FlatBendResult object represents a single bend instance in the flat. A bend instance can result from a feature placed either in the folded model or in the flat pattern. A bend feature may define multiple bends, and every one of the resulting bend instances is represented by a FlatBendResult object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetBendOrder](../FlatBendResult/FlatBendResult_GetBendOrder.md) | Method that gets the bend order for this bend result. |
| [SetBendOrder](../FlatBendResult/FlatBendResult_SetBendOrder.md) | Method that sets the bend order for this bend result. This will define a bend order override for this bend result. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Angle](../FlatBendResult/FlatBendResult_Angle.md) | Property that returns the angle of the bend. |
| [Application](../FlatBendResult/FlatBendResult_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Bend](../FlatBendResult/FlatBendResult_Bend.md) | Property that returns the Bend object associated with this bend result. |
| [Edge](../FlatBendResult/FlatBendResult_Edge.md) | Property that returns the edge in the flat pattern that belongs to the bend result. |
| [InnerRadius](../FlatBendResult/FlatBendResult_InnerRadius.md) | Property that returns the inner radius of the bend. |
| [InternalName](../FlatBendResult/FlatBendResult_InternalName.md) | Property that returns a string that uniquely identifies a bend instance within the flat pattern. |
| [IsDirectionUp](../FlatBendResult/FlatBendResult_IsDirectionUp.md) | Property that returns whether the direction of the bend is up or down. |
| [IsOnBottomFace](../FlatBendResult/FlatBendResult_IsOnBottomFace.md) | Property that returns whether this bend result is on the bottom face of the flat pattern. Every bend has two coresponding bend results on the flat pattern one on the top face and one on the bottom face. |
| [kFactor](../FlatBendResult/FlatBendResult_kFactor.md) | Read-only property that returns the K-Factor value associated with this bend. |
| [Parent](../FlatBendResult/FlatBendResult_Parent.md) | Property that returns the parent FlatPattern object. |
| [Type](../FlatBendResult/FlatBendResult_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FlatBendResults.Item](../FlatBendResults/FlatBendResults_Item.md), [FlatPatternPlate.GetBendResult](FlatPatternPlate_GetBendResult.md)

## Version

Introduced in version 2008
