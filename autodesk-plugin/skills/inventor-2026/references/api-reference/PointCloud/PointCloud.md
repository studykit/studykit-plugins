# PointCloud Object

## Description

The PointCloud object represents a single point cloud within Inventor.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../PointCloud/PointCloud_Delete.md) | Method that deletes the point cloud. |
| [GetReferenceKey](../PointCloud/PointCloud_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |
| [ModelToPointCloudSpace](../PointCloud/PointCloud_ModelToPointCloudSpace.md) | Method that takes a 3d coordinate in model space and returns a Point object containing the coordinate point in point cloud space. |
| [PointCloudToModelSpace](../PointCloud/PointCloud_PointCloudToModelSpace.md) | Method that takes a 3d coordinate in point cloud space and returns a Point object containing the coordinate point in model space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PointCloud/PointCloud_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PointCloud/PointCloud_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [Crops](../PointCloud/PointCloud_Crops.md) | Read-only property that returns the PointCloudCrops collection object. |
| [Density](../PointCloud/PointCloud_Density.md) | Read-write property that gets and sets the density of the points displayed. The range of this property is from 1 to 10. |
| [DisplayedPointCount](../PointCloud/PointCloud_DisplayedPointCount.md) | Read-only property that returns the total number of cloud points currently being displayed. This is the result of the density, MaximumPointCount and cropping. |
| [HealthStatus](../PointCloud/PointCloud_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [MaximumPointCount](../PointCloud/PointCloud_MaximumPointCount.md) | Read-write property that gets and sets the maximum point count that can be displayed in current point cloud. |
| [Name](../PointCloud/PointCloud_Name.md) | Read-only property that returns the name of the point cloud. This is the name that’s visible in the browser. |
| [Parent](../PointCloud/PointCloud_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [RangeBox](../PointCloud/PointCloud_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [RangeBoxInPointCloudSpace](../PointCloud/PointCloud_RangeBoxInPointCloudSpace.md) | Read-only property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object in point cloud space. |
| [Regions](../PointCloud/PointCloud_Regions.md) | Read-only property that returns the point cloud regions collection object. |
| [Scale](../PointCloud/PointCloud_Scale.md) | Read-write property that gets and sets the scale of the point cloud. |
| [Scans](../PointCloud/PointCloud_Scans.md) | Read-only property that returns the point cloud scans collection object. |
| [SourceFullFileName](../PointCloud/PointCloud_SourceFullFileName.md) | Read-only property that returns the point cloud source full file name. |
| [TotalPointCount](../PointCloud/PointCloud_TotalPointCount.md) | Read-only property that returns the total number of points in the point cloud taking no account of the crops. |
| [Transform](../PointCloud/PointCloud_Transform.md) | Read-write property that gets and sets the matrix that defines the translation, rotation of the point cloud in model space. |
| [Type](../PointCloud/PointCloud_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsFactor](../PointCloud/PointCloud_UnitsFactor.md) | Read-only property that returns the units ratio between the point cloud source units and the Inventor database length unit(centimeters). |
| [Visible](../PointCloud/PointCloud_Visible.md) | Read-write property that gets and sets the visibility of this point cloud. |

## Accessed From

[PointCloudCrop.Parent](../PointCloudCrop/PointCloudCrop_Parent.md), [PointCloudPlane.Parent](../PointCloudPlane/PointCloudPlane_Parent.md), [PointCloudPlaneProxy.Parent](../PointCloudPlaneProxy/PointCloudPlaneProxy_Parent.md), [PointCloudPoint.Parent](../PointCloudPoint/PointCloudPoint_Parent.md), [PointCloudPointProxy.Parent](../PointCloudPointProxy/PointCloudPointProxy_Parent.md), [PointCloudProxy.NativeObject](../PointCloudProxy/PointCloudProxy_NativeObject.md), [PointCloudRegion.Parent](../PointCloudRegion/PointCloudRegion_Parent.md), [PointClouds.Add](../PointClouds/PointClouds_Add.md), [PointClouds.Item](../PointClouds/PointClouds_Item.md), [PointCloudScan.Parent](../PointCloudScan/PointCloudScan_Parent.md)

## Derived Classes

[PointCloudProxy](../PointCloudProxy/PointCloudProxy.md)

## Version

Introduced in version 2013
