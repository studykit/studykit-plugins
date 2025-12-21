# iFeatures Object

## Description

The iFeatures collection object provides access to all of the iFeature objects in a part component definition and provides methods to create additional iFeatures..

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../iFeatures/iFeatures_Add.md) | Method that creates a new iFeature using the input placement information. If successfully created the new iFeature is returned. |
| [CreateiFeatureDefinition](../iFeatures/iFeatures_CreateiFeatureDefinition.md) | Method that creates a new iFeatrureDefinition. The returned definition provides access to all of the inputs that are necessary for placing an iFeature. Using this object you provide the parameter and the geometry inputs necessary for placing the iFeature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatures/iFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../iFeatures/iFeatures_Count.md) | Property that specifies the number of items in the collection. |
| [Item](../iFeatures/iFeatures_Item.md) | Returns the specified iFeature object from the collection.. |
| [Type](../iFeatures/iFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FlatPatternFeatures.iFeatures](../FlatPatternFeatures/FlatPatternFeatures_iFeatures.md), [PartFeatures.iFeatures](../PartFeatures/PartFeatures_iFeatures.md), [SheetMetalFeatures.iFeatures](../SheetMetalFeatures/SheetMetalFeatures_iFeatures.md)

## Version

Introduced in version 2009
