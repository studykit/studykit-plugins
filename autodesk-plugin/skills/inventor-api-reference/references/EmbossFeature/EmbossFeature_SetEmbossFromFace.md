# EmbossFeature.SetEmbossFromFace Method

Parent Object: [EmbossFeature](../EmbossFeature/EmbossFeature.md)

## Description

Method that redefines the emboss feature by embossing a profile on one or more faces in the model.

## Syntax

EmbossFeature.**SetEmbossFromFace**( ***Distance*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), [***WrapFace***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Distance | Variant | Input Variant that defines the depth of the emboss. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates on which side of the sketch plane the emboss feature should be placed. Valid input is either kPositiveExtentDirection or kNegativeExtentDirection constant value in PartFeatureExtentDirectionEnum. The value kPositiveExtentDirection defines the projection direction of the profile to be in the same direction as the normal of the sketch plane that contains the profile to be embossed. If kSymmetricExtentDirection is specified, then the emboss feature will fail to be redefined. |
| WrapFace | Variant | Optional Input Variant that specifies the face around which the emboss feature should be wrapped. The valid input is a Face object. This argument can be used to specify a curved face around which the emboss feature should be wrapped. The face can only be planar or conical, not a spline. If the emboss profile is large relative to the amount of curvature, the embossed or engraved area distorts slightly as it projects to the curved face. The wrap stops when a perpendicular face is encountered. If this argument is not specified, then it implies that the emboss feature should not be wrapped around any face, but created as a result of straight projection onto the face. |

## Version

Introduced in version 2008
