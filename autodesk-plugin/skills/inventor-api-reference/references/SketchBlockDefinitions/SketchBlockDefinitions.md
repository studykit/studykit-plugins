# SketchBlockDefinitions Object

## Description

The SketchBlockDefinitions collection object provides access to all sketch block definitions and provides methods to create additional definitions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchBlockDefinitions/SketchBlockDefinitions_Add.md) | Method that creates a new (empty) SketchBlockDefinition. The newly created SketchBlockDefinition is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchBlockDefinitions/SketchBlockDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchBlockDefinitions/SketchBlockDefinitions_Count.md) | Property that returns the number of items in this collection. |
| [Item](../SketchBlockDefinitions/SketchBlockDefinitions_Item.md) | Returns the specified SketchBlockDefinition object from the collection. |
| [Type](../SketchBlockDefinitions/SketchBlockDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FlatPattern.SketchBlockDefinitions](../FlatPattern/FlatPattern_SketchBlockDefinitions.md), [PartComponentDefinition.SketchBlockDefinitions](../PartComponentDefinition/PartComponentDefinition_SketchBlockDefinitions.md), [SheetMetalComponentDefinition.SketchBlockDefinitions](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_SketchBlockDefinitions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create and insert a sketch block definition into a part sketch](../../sample-programs/SketchBlockDefinition_Sample.md) | This sample demonstrates inserting a sketch block into a part sketch. |

## Version

Introduced in version 2010
