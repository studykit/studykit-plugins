# FlatPunchResult Object

## Description

The FlatPunchResult object represents a single punch instance in the flat. A punch instance can result from a punch tool feature placed either in the folded model or in the flat pattern. A punch tool feature may define multiple punches, and every one of the resulting punch instances is represented by a FlatPunchResult object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Angle](../FlatPunchResult/FlatPunchResult_Angle.md) | Property that returns an angle value indicating the punch orientation. This property may return an error if this information is not available. |
| [Application](../FlatPunchResult/FlatPunchResult_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Depth](../FlatPunchResult/FlatPunchResult_Depth.md) | Property that returns the depth of the punch. |
| [Faces](../FlatPunchResult/FlatPunchResult_Faces.md) | Property that returns the faces in the flat pattern that belong to the punch result. This property returns Nothing if punch representation is not formed feature representation. |
| [FoldedAngle](../FlatPunchResult/FlatPunchResult_FoldedAngle.md) | Property that returns an angle value indicating the punch orientation in the folded model. |
| [FoldedPosition](../FlatPunchResult/FlatPunchResult_FoldedPosition.md) | Property that returns a Point indicating the position of the punch instance in the folded model. |
| [HasDepth](../FlatPunchResult/FlatPunchResult_HasDepth.md) | Gets whether there is a depth value associated with this punch result. |
| [InternalName](../FlatPunchResult/FlatPunchResult_InternalName.md) | Property that returns a string that uniquely identifies a punch instance within the flat pattern. |
| [IsDirectionUp](../FlatPunchResult/FlatPunchResult_IsDirectionUp.md) | Property that whether the direction of the punch is up or down. |
| [IsPunchAfterStopNode](../FlatPunchResult/FlatPunchResult_IsPunchAfterStopNode.md) | Property that returns whether the punch feature that resulted in this punch result is currently after the stop node. |
| [IsPunchSuppressed](../FlatPunchResult/FlatPunchResult_IsPunchSuppressed.md) | Property that returns whether the punch feature that resulted in this punch result is currently suppressed. |
| [Parent](../FlatPunchResult/FlatPunchResult_Parent.md) | Property that returns the parent FlatPattern object. |
| [Position](../FlatPunchResult/FlatPunchResult_Position.md) | Property that returns a Point indicating the position of the punch instance in the flat pattern. This property may return Nothing if this information is not available. |
| [PunchId](../FlatPunchResult/FlatPunchResult_PunchId.md) | Property that returns the Id associated with the punch result. This is the Id assigned during creation of the punch feature and is the same for all instances of a punch feature. |
| [SketchRepresentationEdges](../FlatPunchResult/FlatPunchResult_SketchRepresentationEdges.md) | Property that returns the edges in the flat pattern that belong to the punch result. The property will return Nothing if the punch tool feature that resulted in this punch result does not have a sketch-based alternate representation defined for it. |
| [Type](../FlatPunchResult/FlatPunchResult_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FlatPunchResults.Item](../FlatPunchResults/FlatPunchResults_Item.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |