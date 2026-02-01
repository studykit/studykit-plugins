# SplitFeatures Object

## Description

The Part SplitFeatures object represents a collection of objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [SplitBody](../SplitFeatures/SplitFeatures_SplitBody.md) | Method that creates a new SplitFeature by splitting a body. The original body is consumed by the operation and two new bodies are created. The new SplitFeature is returned. |
| [SplitFaces](../SplitFeatures/SplitFeatures_SplitFaces.md) | Method that creates a new SplitFeature by splitting faces of a part. The new SplitFeature is returned. |
| [TrimSolid](../SplitFeatures/SplitFeatures_TrimSolid.md) | Method that creates a new SplitFeature by splitting a solid body. The specified portion of the solid is removed. The new SplitFeature is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SplitFeatures/SplitFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SplitFeatures/SplitFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../SplitFeatures/SplitFeatures_Item.md) | Returns the specified SplitFeature object from the collection. |
| [Type](../SplitFeatures/SplitFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartFeatures.SplitFeatures](../PartFeatures/PartFeatures_SplitFeatures.md), [SheetMetalFeatures.SplitFeatures](../SheetMetalFeatures/SheetMetalFeatures_SplitFeatures.md)

## Version

Introduced in version 5
