# CornerRoundDefinition Object

## Description

The CornerRoundDefinition object is a utility object used for creating, querying, and editing sheet metal corner round features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddEdgeSet](../CornerRoundDefinition/CornerRoundDefinition_AddEdgeSet.md) | Method that creates a new edge set within the corner round definition. |
| [Copy](../CornerRoundDefinition/CornerRoundDefinition_Copy.md) | Function that creates a copy of this CornerRoundDefinition object. The copy is independent of any other object and can be edited without affecting anything else. It can then be used as input to either modify an existing corner round or create a new corner round feature. |
| [RemoveEdgeSet](../CornerRoundDefinition/CornerRoundDefinition_RemoveEdgeSet.md) | Method that removes the specified CornerRoundEdgeSet object from this CornerRoundDefinition object. This results in all the corner round being removed from the edges in this edge set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CornerRoundDefinition/CornerRoundDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EdgeSetCount](../CornerRoundDefinition/CornerRoundDefinition_EdgeSetCount.md) | Property that returns the number of edge sets defined within this CornerRoundDefinition object. |
| [EdgeSetItem](../CornerRoundDefinition/CornerRoundDefinition_EdgeSetItem.md) | Method that returns the specified CornerRoundEdgeSet object from this CornerRoundDefinition object. |
| [Parent](../CornerRoundDefinition/CornerRoundDefinition_Parent.md) | Property that returns the parent CornerRoundFeature of this CornerRoundDefinition object. |
| [Type](../CornerRoundDefinition/CornerRoundDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CornerRoundDefinition.Copy](../CornerRoundDefinition/CornerRoundDefinition_Copy.md), [CornerRoundEdgeSet.Parent](../CornerRoundEdgeSet/CornerRoundEdgeSet_Parent.md), [CornerRoundFeature.Definition](../CornerRoundFeature/CornerRoundFeature_Definition.md), [CornerRoundFeatureProxy.Definition](../CornerRoundFeatureProxy/CornerRoundFeatureProxy_Definition.md), [CornerRoundFeatures.CreateCornerRoundDefinition](../CornerRoundFeatures/CornerRoundFeatures_CreateCornerRoundDefinition.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |