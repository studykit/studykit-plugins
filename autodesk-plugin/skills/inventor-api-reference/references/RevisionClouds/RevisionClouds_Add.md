# RevisionClouds.Add Method

Parent Object: [RevisionClouds](../RevisionClouds/RevisionClouds.md)

## Description

Method that creates a new revision cloud.

## Syntax

RevisionClouds.**Add**( ***Definition*** As [RevisionCloudDefinition](../RevisionCloudDefinition/RevisionCloudDefinition.md), [***Name***] As Variant ) As [RevisionCloud](../RevisionCloud/RevisionCloud.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [RevisionCloudDefinition](../RevisionCloudDefinition/RevisionCloudDefinition.md) | Input RevisionCloudDefinition object that defines the revision cloud you want to create. An RevisionCloudDefinition object can be created using the RevisionClouds.CreateRevisionCloudDefinition method. It can also be obtained from an existing RevisionCloud object. |
| Name | Variant | Optional input String value that specifies the name of the new RevisionCloud object. If not specified a default name will be applied. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [RevisionCloud Creation Sample](../../sample-programs/RevisionCloudCreation_Sample.md) | This sample is to demonstrate how to create a revision cloud in drawing document. |

## Version

Introduced in version 2024
