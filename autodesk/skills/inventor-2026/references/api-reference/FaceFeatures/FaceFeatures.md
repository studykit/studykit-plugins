# FaceFeatures Object

## Description

The FaceFeatures collection object provides access to all of the objects in a sheet metal component definition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../FaceFeatures/FaceFeatures_Add.md) | Method that creates a new face feature. The newly created FaceFeature object is returned. |
| [CreateFaceFeatureDefinition](../FaceFeatures/FaceFeatures_CreateFaceFeatureDefinition.md) | Method that creates a new FaceFeatureDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FaceFeatures/FaceFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../FaceFeatures/FaceFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../FaceFeatures/FaceFeatures_Item.md) | Returns the specified FaceFeature object from the collection. This is the default property of the FaceFeatures collection object. |
| [Type](../FaceFeatures/FaceFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SheetMetalFeatures.FaceFeatures](../SheetMetalFeatures/SheetMetalFeatures_FaceFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 5.3
