# LoftFeatures Object

## Description

The LoftFeatures collection object provides access to existing loft features and supports the ability to create new loft features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../LoftFeatures/LoftFeatures_Add.md) | Method that creates a new loft. |
| [CreateLoftDefinition](../LoftFeatures/LoftFeatures_CreateLoftDefinition.md) | Method that creates a LoftDefinition object that defines the input definition for a loft feature. |
| [CreateMapCurves](../LoftFeatures/LoftFeatures_CreateMapCurves.md) | Method that creates a new MapPointCurves object. You then use functionality provided by the resulting MapPointCurves object to define the specific point mapping. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../LoftFeatures/LoftFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../LoftFeatures/LoftFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../LoftFeatures/LoftFeatures_Item.md) | Returns the specified LoftFeature object from the collection. |
| [Type](../LoftFeatures/LoftFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartFeatures.LoftFeatures](../PartFeatures/PartFeatures_LoftFeatures.md), [SheetMetalFeatures.LoftFeatures](../SheetMetalFeatures/SheetMetalFeatures_LoftFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 5
