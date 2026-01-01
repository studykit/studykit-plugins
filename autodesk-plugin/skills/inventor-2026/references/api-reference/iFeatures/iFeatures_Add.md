# iFeatures.Add Method

Parent Object: [iFeatures](../iFeatures/iFeatures.md)

## Description

Method that creates a new iFeature using the input placement information. If successfully created the new iFeature is returned.

## Syntax

iFeatures.**Add**( ***Definition*** As [iFeatureDefinition](../iFeatureDefinition/iFeatureDefinition.md) ) As [iFeature](../iFeature/iFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [iFeatureDefinition](../iFeatureDefinition/iFeatureDefinition.md) | Input iFeatureDefinition object used to define the various input required for the placement of an iFeature. Appropriate input must be defined in the iFeatureDefinition object in order to place the iFeature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Placement of a standard iFeature](../../sample-programs/iFeatures_Sample.md) | This program demonstrates the placement of a standard iFeature in a part. |
| [Place table driven iFeature](../../sample-programs/iFeatureTable_Sample.md) | This program demonstrates the placement of a table driven iFeature in a part. |

## Version

Introduced in version 2009
