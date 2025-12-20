# FaceFeatures.CreateFaceFeatureDefinition Method

Parent Object: [FaceFeatures](../FaceFeatures/FaceFeatures.md)

## Description

Method that creates a new FaceFeatureDefinition object.

## Remarks

This object is not a face feature but contains the information that defines a face feature and can be used to create a new face feature or edit an existing one. The returned FaceFeatureDefinition can be used as input to the FaceFeatures.Add method to create a new face feature. You can edit the properties of the FaceFeatureDefinition object before creating the face feature to get the desired face feature.

## Syntax

FaceFeatures.**CreateFaceFeatureDefinition**( ***Profile*** As [Profile](../Profile/Profile.md) ) As [FaceFeatureDefinition](../FaceFeatureDefinition/FaceFeatureDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object that defines the shape of the face. The input profile must consist of one or more closed paths. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |