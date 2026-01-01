# RibFeatures Object

## Description

The Part RibFeatures collection object. A is a closed, thin-walled support shape.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../RibFeatures/RibFeatures_Add.md) | Method that creates a new Rib feature. The newly created RibFeature object is returned. |
| [CreateDefinition](../RibFeatures/RibFeatures_CreateDefinition.md) | Method that creates a new RibDefinition object. The object created does not represent a rib feature but instead is a representation of the information that defines a rib feature. You can use this object as input to the RibFeatures.Add method to create the actual feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RibFeatures/RibFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../RibFeatures/RibFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../RibFeatures/RibFeatures_Item.md) | Returns the specified object in the collection. The index can be numeric or the object name. |
| [Type](../RibFeatures/RibFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartFeatures.RibFeatures](../PartFeatures/PartFeatures_RibFeatures.md), [SheetMetalFeatures.RibFeatures](../SheetMetalFeatures/SheetMetalFeatures_RibFeatures.md)

## Version

Introduced in version 5
