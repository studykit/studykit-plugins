# PointCloudProxy Object

Derived from: [PointCloud](../PointCloud/PointCloud.md) Object

## Description

PointCloudProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../PointCloudProxy/PointCloudProxy_Delete.md) | Method that deletes the point cloud. |
| [GetReferenceKey](../PointCloudProxy/PointCloudProxy_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |
| [ModelToPointCloudSpace](../PointCloudProxy/PointCloudProxy_ModelToPointCloudSpace.md) | Method that takes a 3d coordinate in model space and returns a Point object containing the coordinate point in point cloud space. |
| [PointCloudToModelSpace](../PointCloudProxy/PointCloudProxy_PointCloudToModelSpace.md) | Method that takes a 3d coordinate in point cloud space and returns a Point object containing the coordinate point in model space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PointCloudProxy/PointCloudProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PointCloudProxy/PointCloudProxy_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [ContainingOccurrence](../PointCloudProxy/PointCloudProxy_ContainingOccurrence.md) | Get the component occurrence context through which the native object is being seen through. |
| [Crops](../PointCloudProxy/PointCloudProxy_Crops.md) | Read-only property that returns the PointCloudCrops collection object. |
| [Density](../PointCloudProxy/PointCloudProxy_Density.md) | Read-write property that gets and sets the density of the points displayed. The range of this property is from 1 to 10. |
| [DisplayedPointCount](../PointCloudProxy/PointCloudProxy_DisplayedPointCount.md) | Read-only property that returns the total number of cloud points currently being displayed. This is the result of the density, MaximumPointCount and cropping. |
| [HealthStatus](../PointCloudProxy/PointCloudProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [MaximumPointCount](../PointCloudProxy/PointCloudProxy_MaximumPointCount.md) | Read-write property that gets and sets the maximum point count that can be displayed in current point cloud. |
| [Name](../PointCloudProxy/PointCloudProxy_Name.md) | Read-only property that returns the name of the point cloud. This is the name that’s visible in the browser. |
| [NativeObject](../PointCloudProxy/PointCloudProxy_NativeObject.md) | Get the source object in the context of the definition instead of the containing assembly. |
| [Parent](../PointCloudProxy/PointCloudProxy_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [RangeBox](../PointCloudProxy/PointCloudProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [RangeBoxInPointCloudSpace](../PointCloudProxy/PointCloudProxy_RangeBoxInPointCloudSpace.md) | Read-only property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object in point cloud space. |
| [Regions](../PointCloudProxy/PointCloudProxy_Regions.md) | Read-only property that returns the point cloud regions collection object. |
| [Scale](../PointCloudProxy/PointCloudProxy_Scale.md) | Read-write property that gets and sets the scale of the point cloud. |
| [Scans](../PointCloudProxy/PointCloudProxy_Scans.md) | Read-only property that returns the point cloud scans collection object. |
| [SourceFullFileName](../PointCloudProxy/PointCloudProxy_SourceFullFileName.md) | Read-only property that returns the point cloud source full file name. |
| [TotalPointCount](../PointCloudProxy/PointCloudProxy_TotalPointCount.md) | Read-only property that returns the total number of points in the point cloud taking no account of the crops. |
| [Transform](../PointCloudProxy/PointCloudProxy_Transform.md) | Read-write property that gets and sets the matrix that defines the translation, rotation of the point cloud in model space. |
| [Type](../PointCloudProxy/PointCloudProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsFactor](../PointCloudProxy/PointCloudProxy_UnitsFactor.md) | Read-only property that returns the units ratio between the point cloud source units and the Inventor database length unit(centimeters). |
| [Visible](../PointCloudProxy/PointCloudProxy_Visible.md) | Read-write property that gets and sets the visibility of this point cloud. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |