# RevisionClouds.CreateRevisionCloudDefinition Method

Parent Object: [RevisionClouds](../RevisionClouds/RevisionClouds.md)

## Description

Method that creates a new RevisionCloudDefinition object.

## Syntax

RevisionClouds.**CreateRevisionCloudDefinition**( ***ControlPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***Layer***] As Variant, [***Inverted***] As Boolean ) As [RevisionCloudDefinition](../RevisionCloudDefinition/RevisionCloudDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ControlPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection including Point2d objects that specify the control points to create revision cloud. |
| Layer | Variant | Optional input Layer object that specifies Layer for the revision cloud. If not provided, a default Layer will be used. |
| Inverted | Boolean | Optional input Boolean value that specifies whether to invert the revision cloud or not. If not provided, this defaults to False.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [RevisionCloud Creation Sample](../../sample-programs/RevisionCloudCreation_Sample.md) | This sample is to demonstrate how to create a revision cloud in drawing document. |

## Version

Introduced in version 2024
