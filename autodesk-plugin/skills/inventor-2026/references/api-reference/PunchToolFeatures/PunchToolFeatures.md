# PunchToolFeatures Object

## Description

The PunchToolFeatures collection object provides access to all of the objects in a sheet metal component definition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../PunchToolFeatures/PunchToolFeatures_Add.md) | Creates a new PunchToolFeature using the input placement information. |
| [CreateiFeatureDefinition](../PunchToolFeatures/PunchToolFeatures_CreateiFeatureDefinition.md) | Method that creates a new iFeatureDefinition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PunchToolFeatures/PunchToolFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../PunchToolFeatures/PunchToolFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../PunchToolFeatures/PunchToolFeatures_Item.md) | Returns the specified PunchToolFeature object from the collection. This is the default property of the PunchToolFeatures collection object. |
| [Type](../PunchToolFeatures/PunchToolFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FlatPatternFeatures.PunchToolFeatures](../FlatPatternFeatures/FlatPatternFeatures_PunchToolFeatures.md), [SheetMetalFeatures.PunchToolFeatures](../SheetMetalFeatures/SheetMetalFeatures_PunchToolFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |

## Version

Introduced in version 5.3
