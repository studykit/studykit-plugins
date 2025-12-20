# FlangeFeatures Object

## Description

The FlangeFeatures collection object provides access to all of the objects in a sheet metal component definition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../FlangeFeatures/FlangeFeatures_Add.md) | Method that creates a new flange feature. The newly created FlangeFeature object is returned. |
| [CreateDefinition](../FlangeFeatures/FlangeFeatures_CreateDefinition.md) | Method that creates a new FlangeDefinition object. The object created does not represent a flange feature but instead is a representation of the information that defines a flange feature. You can use this object as input to the FlangeFeatures.Add method to cr. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FlangeFeatures/FlangeFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../FlangeFeatures/FlangeFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../FlangeFeatures/FlangeFeatures_Item.md) | Returns the specified FlangeFeature object from the collection. This is the default property of the FlangeFeatures collection object. |
| [Type](../FlangeFeatures/FlangeFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SheetMetalFeatures.FlangeFeatures](../SheetMetalFeatures/SheetMetalFeatures_FlangeFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |