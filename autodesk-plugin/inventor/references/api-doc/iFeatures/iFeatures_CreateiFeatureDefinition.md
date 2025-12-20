# iFeatures.CreateiFeatureDefinition Method

Parent Object: [iFeatures](../iFeatures/iFeatures.md)

## Description

Method that creates a new iFeatrureDefinition. The returned definition provides access to all of the inputs that are necessary for placing an iFeature. Using this object you provide the parameter and the geometry inputs necessary for placing the iFeature.

## Syntax

iFeatures.**CreateiFeatureDefinition**( ***FullFileName*** As String ) As [iFeatureDefinition](../iFeatureDefinition/iFeatureDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input string that specifies the name of the iFeature file (.ide) to create the definition for. The file must be an existing iFeature file. If an invalid file is specified an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Placement of a standard iFeature](../../sample-programs/iFeatures_Sample.md) | This program demonstrates the placement of a standard iFeature in a part. |
| [Place table driven iFeature](../../sample-programs/iFeatureTable_Sample.md) | This program demonstrates the placement of a table driven iFeature in a part. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |