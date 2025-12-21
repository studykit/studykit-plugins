# FaceFeatures.Add Method

Parent Object: [FaceFeatures](../FaceFeatures/FaceFeatures.md)

## Description

Method that creates a new face feature. The newly created FaceFeature object is returned.

## Syntax

FaceFeatures.**Add**( ***FaceFeatureDefinition*** As [FaceFeatureDefinition](../FaceFeatureDefinition/FaceFeatureDefinition.md) ) As [FaceFeature](../FaceFeature/FaceFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FaceFeatureDefinition | [FaceFeatureDefinition](../FaceFeatureDefinition/FaceFeatureDefinition.md) | Input FaceFeatureDefinition object that defines the face feature you want to create. A FaceFeatureDefinition object can be created using the FaceFeatures.CreateFaceFeatureDefinition method. It can also be obtained from an existing FaceFeature object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 2009
