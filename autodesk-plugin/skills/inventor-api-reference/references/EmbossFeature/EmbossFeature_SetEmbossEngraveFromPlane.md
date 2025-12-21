# EmbossFeature.SetEmbossEngraveFromPlane Method

Parent Object: [EmbossFeature](../EmbossFeature/EmbossFeature.md)

## Description

Method that redefines the emboss feature by embossing and/or engraving a profile on one or more faces in the model.

## Syntax

EmbossFeature.**SetEmbossEngraveFromPlane**( ***Taper*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Taper | Variant | Input Variant that defines the taper angle of the emboss. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates on which side of the sketch plane the emboss feature should be placed. Valid input is one of the constants in PartFeatureExtentDirectionEnum: kPositiveExtentDirection, kNegativeExtentDirection or kSymmetricExtentDirection. The value kPositiveExtentDirection defines the emboss direction to be in the same direction as the normal of the sketch plane that contains the profile to be embossed. |

## Version

Introduced in version 2008
