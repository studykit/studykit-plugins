# PointClouds.Add Method

Parent Object: [PointClouds](../PointClouds/PointClouds.md)

## Description

Method that creates a new point cloud. The newly created PointCloud object is returned.

## Remarks

Valid values for the NameValueMap in the Options argument:

| Name | Type | Notes |
| --- | --- | --- |
| Density | Long | The density that defines the percentage of points to initially display. Valid value is from 1 to 10. If not specified this will default to 10. |
| MaximumPointCount | Long | The value of the maximum point count being displayed. If the MaximumPointCount is specified in Options, the displayed point count should be no more than the MaximumPointCount or the value calculated with the Density, whichever is smaller. |

## Syntax

PointClouds.**Add**( ***PointCloudFilename*** As String, [***Transform***] As Variant, [***Scale***] As Variant, [***Options***] As Variant ) As [PointCloud](../PointCloud/PointCloud.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointCloudFilename | String | Input full filename of a point cloud file. |
| Transform | Variant | Optional input Matrix that defines the position and orientation of the point cloud in the model space. The matrix must only define translation, rotation, and uniform scale. If not provided an identity matrix is used which will result in the point cloud being aligned with model space and full scale. |
| Scale | Variant | Optional input Double that defines the scale of the point cloud. If not specified the default value of 1 will be used.   This is an optional argument whose default value is null. |
| Options | Variant | Optional input NameValueMap that specifies additional options for add.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2016
