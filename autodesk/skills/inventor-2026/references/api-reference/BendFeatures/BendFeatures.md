# BendFeatures Object

## Description

The BendFeatures collection object provides access to all of the objects in a sheet metal component definition. It"s also through the BendFeatures object that you create new BendFeature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../BendFeatures/BendFeatures_Add.md) | Method that creates a new bend feature. The newly created BendFeature object is returned. |
| [CreateBendDefinition](../BendFeatures/BendFeatures_CreateBendDefinition.md) | Method that creates a new BendDefinition object. This object is not a bend feature but contains the information that defines bend information and can be used to help create a new feature that contains bends or edit the bend of an existing feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BendFeatures/BendFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../BendFeatures/BendFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../BendFeatures/BendFeatures_Item.md) | Returns the specified BendFeature object from the collection. This is the default property of the BendFeatures collection object. |
| [Type](../BendFeatures/BendFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SheetMetalFeatures.BendFeatures](../SheetMetalFeatures/SheetMetalFeatures_BendFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 5.3
