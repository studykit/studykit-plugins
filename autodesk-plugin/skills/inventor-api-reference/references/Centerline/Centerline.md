# Centerline Object

## Description

The Centerline object represents a centerline on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Centerline/Centerline_Delete.md) | Method that deletes the Centerline. |
| [GetBisectorEntities](../Centerline/Centerline_GetBisectorEntities.md) | Returns the two entities that the centerline bisects. This method is only valid for kBisectorCenterline type centerlines and will fail in all other cases. |
| [GetReferenceKey](../Centerline/Centerline_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Centerline/Centerline_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Attached](../Centerline/Centerline_Attached.md) | Property that returns whether the centerline is sick. Returns False if the centerline is sick. |
| [AttributeSets](../Centerline/Centerline_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterlineType](../Centerline/Centerline_CenterlineType.md) | Property that gets the centerline type. This could return kRegularCenterline, kBisectorCenterline, kCenteredPatternCenterline or kWorkFeatureCenterline. If the property returns kWorkFeatureCenterline, the centerline is associated with a model work feature. The work feature can be obtained using the ModelWorkFeature property. |
| [EndPoint](../Centerline/Centerline_EndPoint.md) | Read-write property that gets and sets the end point of the centerline. |
| [FitPoints](../Centerline/Centerline_FitPoints.md) | Property that returns the collection of objects that define the path of the centerline. |
| [Geometry](../Centerline/Centerline_Geometry.md) | Property that returns the geometry that defines the shape of the centerline object. |
| [GeometryType](../Centerline/Centerline_GeometryType.md) | Property that returns the type of the curve used to define the centerline. This property allows you to determine what type of object will be returned by the Geometry. |
| [Layer](../Centerline/Centerline_Layer.md) | Gets and sets the layer associated with this object. |
| [ModelWorkFeature](../Centerline/Centerline_ModelWorkFeature.md) | Property that returns the model work feature associated with this centerline. This property returns Nothing if the CenterlineType property is not kWorkFeatureCenterline. |
| [Parent](../Centerline/Centerline_Parent.md) | Property that returns the parent Sheet object. |
| [PatternCenter](../Centerline/Centerline_PatternCenter.md) | Property that returns the geometry the center that defines the center of the centerline pattern. This property is only valid for kCenteredPatternCenterline type centerlines and will return Nothing in all other cases. |
| [StartPoint](../Centerline/Centerline_StartPoint.md) | Read-write property that gets and sets the start point of the centerline. |
| [Style](../Centerline/Centerline_Style.md) | Gets and sets the style associated with this centerline. |
| [Type](../Centerline/Centerline_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../Centerline/Centerline_Visible.md) | Read-write property that gets and sets whether the centerline is visible. |

## Accessed From

[Centerlines.Add](../Centerlines/Centerlines_Add.md), [Centerlines.AddBisector](../Centerlines/Centerlines_AddBisector.md), [Centerlines.AddByWorkFeature](../Centerlines/Centerlines_AddByWorkFeature.md), [Centerlines.AddCenteredPattern](../Centerlines/Centerlines_AddCenteredPattern.md), [Centerlines.Item](../Centerlines/Centerlines_Item.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |