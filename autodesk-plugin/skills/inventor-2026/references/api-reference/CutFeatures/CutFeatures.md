# CutFeatures Object

## Description

The CutFeatures collection object provides access to the CutFeature objects. It"s also through the CutFeatures object that you create new CutFeature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../CutFeatures/CutFeatures_Add.md) | Method that creates a new cut feature. |
| [CreateCutDefinition](../CutFeatures/CutFeatures_CreateCutDefinition.md) | Method that creates a new CutDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CutFeatures/CutFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../CutFeatures/CutFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../CutFeatures/CutFeatures_Item.md) | Returns the specified CutFeature object from the collection. This is the default property of the CutFeatures collection object. |
| [Type](../CutFeatures/CutFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FlatPatternFeatures.CutFeatures](../FlatPatternFeatures/FlatPatternFeatures_CutFeatures.md), [SheetMetalFeatures.CutFeatures](../SheetMetalFeatures/SheetMetalFeatures_CutFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 5.3
