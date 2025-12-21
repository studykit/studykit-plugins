# EmbossFeatures.AddEmbossEngraveFromPlane Method

Parent Object: [EmbossFeatures](../EmbossFeatures/EmbossFeatures.md)

## Description

Method that creates a new emboss feature by embossing and/or engraving a profile on one or more faces in the model.

## Remarks

If the emboss feature is created successfully, an EmbossFeature object corresponding to the newly created emboss feature is returned from this method.

## Syntax

EmbossFeatures.**AddEmbossEngraveFromPlane**( ***Profile*** As [Profile](../Profile/Profile.md), ***Taper*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), [***TopFaceColor***] As Variant ) As [EmbossFeature](../EmbossFeature/EmbossFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object used to define the shape of the emboss. The specified profile must be closed, otherwise (i.e. if the profile is open), the creation of the emboss feature will fail. The closed profiles can constitute both sketch entities as well as text. |
| Taper | Variant | Input Variant that defines the taper angle of the emboss. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates on which side of the sketch plane the emboss feature should be created. The profile will be extended to create the emboss feature starting from the sketch plane until any existing face in the model is intersected. Valid input is any one of the constants in PartFeatureExtentDirectionEnum: kPositiveExtentDirection, kNegativeExtentDirection or kSymmetricExtentDirection. The value kPositiveExtentDirection defines the emboss direction to be in the same direction as the normal of the sketch plane that contains the profile to be embossed. |
| TopFaceColor | Variant | Optional Input Variant that defines the render style to use for the top face of the emboss feature. The valid input is a RenderStyle object. If no input is specified, then the default render style will be applied. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |