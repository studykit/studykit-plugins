# BendFeatures.Add Method

Parent Object: [BendFeatures](../BendFeatures/BendFeatures.md)

## Description

Method that creates a new bend feature. The newly created BendFeature object is returned.

## Syntax

BendFeatures.**Add**( ***BendDefinition*** As [BendDefinition](../BendDefinition/BendDefinition.md) ) As [BendFeature](../BendFeature/BendFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BendDefinition | [BendDefinition](../BendDefinition/BendDefinition.md) | Input BendDefinition object that defines the bend feature you want to create. A BendDefinition object can be created using the BendFeatures.CreateBendDefinition method. It can also be obtained from an existing feature that has an associated bend. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 2010
