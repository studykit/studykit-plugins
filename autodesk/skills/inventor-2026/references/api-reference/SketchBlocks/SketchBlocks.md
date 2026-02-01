# SketchBlocks Object

## Description

The SketchBlocks collection object provides access to all sketch block instances within a sketch and provides methods to create additional block instances.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchBlocks/SketchBlocks_Add.md) | Method that creates a sketch block instance using existing sketch objects. A sketch block definition is implicitly created. The newly created SketchBlock object is returned. |
| [AddByDefinition](../SketchBlocks/SketchBlocks_AddByDefinition.md) | Method that creates a sketch block instance based on the \input definition. The newly created SketchBlock object is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchBlocks/SketchBlocks_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchBlocks/SketchBlocks_Count.md) | Property that returns the number of items in this collection. |
| [Item](../SketchBlocks/SketchBlocks_Item.md) | Returns the specified SketchBlock object from the collection. |
| [Type](../SketchBlocks/SketchBlocks_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PlanarSketch.SketchBlocks](../PlanarSketch/PlanarSketch_SketchBlocks.md), [PlanarSketchProxy.SketchBlocks](../PlanarSketchProxy/PlanarSketchProxy_SketchBlocks.md), [SketchBlockDefinition.SketchBlocks](../SketchBlockDefinition/SketchBlockDefinition_SketchBlocks.md), [SketchBlockDefinitionProxy.SketchBlocks](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_SketchBlocks.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create and insert a sketch block definition into a part sketch](../../sample-programs/SketchBlockDefinition_Sample.md) | This sample demonstrates inserting a sketch block into a part sketch. |
| [Create sketch block from an existing sketch](../../sample-programs/SketchBlocks_Add_Sample.md) | This sample demonstrates creating a sketch block from an existing sketch. |

## Version

Introduced in version 2010
