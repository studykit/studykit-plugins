# FlangeDefinition.SetLegacyDistanceHeightExtent Method

Parent Object: [FlangeDefinition](../FlangeDefinition/FlangeDefinition.md)

## Description

Method that changes the FlangeDefinition object to define a flange whose height is measured by a distance. The way the distance is computed for this type of height extent was used in earlier versions of Inventor and is supported in the current versions to support backward compatibility with older models.

## Syntax

FlangeDefinition.**SetLegacyDistanceHeightExtent**( ***Distance*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***HeightDatumType*** As [HeightDatumTypeEnum](../HeightDatumTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Distance | Variant | Input Variant that defines the distance used for the height extent of the flange. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input value from PartFeatureExtentDirectionEnum that defines the direction of the flange. kPositiveExtentDirection indicates that the direction of the flange is on the side of the selected edge. kNegativeExtentDirection indicates the flange is on the opposite side of the select edge. kSymmetricExtentDirection is not valid for a flange direction. |
| HeightDatumType | [HeightDatumTypeEnum](../HeightDatumTypeEnum.md) | HeightDatumTypeEnum |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |