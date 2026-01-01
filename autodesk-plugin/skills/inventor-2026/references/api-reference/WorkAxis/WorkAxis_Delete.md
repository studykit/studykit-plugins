# WorkAxis.Delete Method

Parent Object: [WorkAxis](../WorkAxis/WorkAxis.md)

## Description

Method that deletes the work axis. Optionally the dependent objects will be deleted. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case.

## Syntax

WorkAxis.**Delete**( [***RetainDependents***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RetainDependents | Boolean | Optional input Boolean that specifies whether any dependent objects should also be deleted. If True, no dependent objects will be deleted. This argument is ignored in the case of an assembly work plane. |

## Version

Introduced in version 4
