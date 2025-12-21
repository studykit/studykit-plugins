# SculptFeatures Object

## Description

The SculptFeatures collection object provides access to all of the SculptFeature objects in a part component definition and provides methods to create additional SculptFeatures.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SculptFeatures/SculptFeatures_Add.md) | Method that creates a new SculptFeature. If the sculpt feature is created successfully, a SculptFeature object corresponding to the newly created sculpt feature is returned from this method. |
| [CreateSculptSurface](../SculptFeatures/SculptFeatures_CreateSculptSurface.md) | Method that creates a new SculptSurface object. The new SculptSurface is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SculptFeatures/SculptFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SculptFeatures/SculptFeatures_Count.md) | Property that specifies the number of items in the collection. |
| [Item](../SculptFeatures/SculptFeatures_Item.md) | Method that returns the specified SculptFeature object from the collection. |
| [Type](../SculptFeatures/SculptFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartFeatures.SculptFeatures](../PartFeatures/PartFeatures_SculptFeatures.md), [SheetMetalFeatures.SculptFeatures](../SheetMetalFeatures/SheetMetalFeatures_SculptFeatures.md)

## Version

Introduced in version 11
