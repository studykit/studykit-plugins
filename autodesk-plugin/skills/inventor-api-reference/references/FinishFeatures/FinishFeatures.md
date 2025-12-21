# FinishFeatures Object

## Description

Finish Features Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../FinishFeatures/FinishFeatures_Add.md) | Method that creates a new finish feature. The newly created FinishFeature object is returned. |
| [CreateDefinition](../FinishFeatures/FinishFeatures_CreateDefinition.md) | Method that creates a new FinishDefinition object. The object created does not represent a finish feature but instead is a representation of the information that defines a finish feature. You can use this object as input to the FinishFeatures.Add method to cre. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FinishFeatures/FinishFeatures_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../FinishFeatures/FinishFeatures_Count.md) | Gets the number of items in this collection. |
| [Item](../FinishFeatures/FinishFeatures_Item.md) | Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well. |
| [Type](../FinishFeatures/FinishFeatures_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[Features.FinishFeatures](../Features/Features_FinishFeatures.md), [PartFeatures.FinishFeatures](../PartFeatures/PartFeatures_FinishFeatures.md), [SheetMetalFeatures.FinishFeatures](../SheetMetalFeatures/SheetMetalFeatures_FinishFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Finish Feature Creation](../../sample-programs/FinishFeatureCreation_Sample.md) | This sample demonstrates how to create a finish feature. |

## Version

Introduced in version 2024
