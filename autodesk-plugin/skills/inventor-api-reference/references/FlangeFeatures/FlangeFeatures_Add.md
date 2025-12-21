# FlangeFeatures.Add Method

Parent Object: [FlangeFeatures](../FlangeFeatures/FlangeFeatures.md)

## Description

Method that creates a new flange feature. The newly created FlangeFeature object is returned.

## Syntax

FlangeFeatures.**Add**( ***FlangeDefinition*** As [FlangeDefinition](../FlangeDefinition/FlangeDefinition.md) ) As [FlangeFeature](../FlangeFeature/FlangeFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FlangeDefinition | [FlangeDefinition](../FlangeDefinition/FlangeDefinition.md) | Input FlangeDefinition object that defines the flange feature you want to create. A FlangeDefinition object can be created using the FlangeFeatures.CreateFlangeDefinition method. It can also be obtained from an existing FlangeFeature object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating flange features](../../sample-programs/FlangeDefinition_SetOffsetWidthExtent_Sample.md) | Demonstrates creating flange features of various width extents. This creates a new document, creates a face feature and adds a flange feature on four edges. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 2011
