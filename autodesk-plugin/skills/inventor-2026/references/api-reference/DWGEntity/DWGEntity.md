# DWGEntity Object

## Description

DWGEntity Object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DWGEntity/DWGEntity_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [HandleID](../DWGEntity/DWGEntity_HandleID.md) | Read-only property that returns the HandleID for the DWGEntity. |
| [Parent](../DWGEntity/DWGEntity_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ParentEntity](../DWGEntity/DWGEntity_ParentEntity.md) | Read-only property that returns the parent DWGEntity of the entity. |
| [Type](../DWGEntity/DWGEntity_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[DWGAcadSupportedProxy.ParentEntity](../DWGAcadSupportedProxy/DWGAcadSupportedProxy_ParentEntity.md), [DWGAcadSupportedProxyProxy.ParentEntity](../DWGAcadSupportedProxyProxy/DWGAcadSupportedProxyProxy_ParentEntity.md), [DWGACMStandardPart.ParentEntity](../DWGACMStandardPart/DWGACMStandardPart_ParentEntity.md), [DWGACMStandardPartProxy.ParentEntity](../DWGACMStandardPartProxy/DWGACMStandardPartProxy_ParentEntity.md), [DWGArc.ParentEntity](../DWGArc/DWGArc_ParentEntity.md), [DWGArcProxy.ParentEntity](../DWGArcProxy/DWGArcProxy_ParentEntity.md), [DWGBlockReference.ParentEntity](../DWGBlockReference/DWGBlockReference_ParentEntity.md), [DWGBlockReferenceProxy.ParentEntity](../DWGBlockReferenceProxy/DWGBlockReferenceProxy_ParentEntity.md), [DWGEllipticalArc.ParentEntity](../DWGEllipticalArc/DWGEllipticalArc_ParentEntity.md), [DWGEllipticalArcProxy.ParentEntity](../DWGEllipticalArcProxy/DWGEllipticalArcProxy_ParentEntity.md), [DWGEntitiesEnumerator.Item](../DWGEntitiesEnumerator/DWGEntitiesEnumerator_Item.md), [DWGEntity.ParentEntity](../DWGEntity/DWGEntity_ParentEntity.md), [DWGEntityArcSegment.Parent](../DWGEntityArcSegment/DWGEntityArcSegment_Parent.md), [DWGEntityEllipticalArcSegment.Parent](../DWGEntityEllipticalArcSegment/DWGEntityEllipticalArcSegment_Parent.md), [DWGEntityLineSegment.Parent](../DWGEntityLineSegment/DWGEntityLineSegment_Parent.md), [DWGEntityProxy.NativeObject](../DWGEntityProxy/DWGEntityProxy_NativeObject.md), [DWGEntityProxy.ParentEntity](../DWGEntityProxy/DWGEntityProxy_ParentEntity.md), [DWGEntitySegment.Parent](../DWGEntitySegment/DWGEntitySegment_Parent.md), [DWGEntitySegmentProxy.ParentEntity](../DWGEntitySegmentProxy/DWGEntitySegmentProxy_ParentEntity.md), [DWGEntitySplineSegment.Parent](../DWGEntitySplineSegment/DWGEntitySplineSegment_Parent.md), [DWGLine.ParentEntity](../DWGLine/DWGLine_ParentEntity.md), [DWGLineProxy.ParentEntity](../DWGLineProxy/DWGLineProxy_ParentEntity.md), [DWGPoint.ParentEntity](../DWGPoint/DWGPoint_ParentEntity.md), [DWGPointProxy.ParentEntity](../DWGPointProxy/DWGPointProxy_ParentEntity.md), [DWGPolyline.ParentEntity](../DWGPolyline/DWGPolyline_ParentEntity.md), [DWGPolyline2D.ParentEntity](../DWGPolyline2D/DWGPolyline2D_ParentEntity.md), [DWGPolyline2DProxy.ParentEntity](../DWGPolyline2DProxy/DWGPolyline2DProxy_ParentEntity.md), [DWGPolyline3D.ParentEntity](../DWGPolyline3D/DWGPolyline3D_ParentEntity.md), [DWGPolyline3DProxy.ParentEntity](../DWGPolyline3DProxy/DWGPolyline3DProxy_ParentEntity.md), [DWGPolylineProxy.ParentEntity](../DWGPolylineProxy/DWGPolylineProxy_ParentEntity.md), [DWGSpline.ParentEntity](../DWGSpline/DWGSpline_ParentEntity.md), [DWGSplineProxy.ParentEntity](../DWGSplineProxy/DWGSplineProxy_ParentEntity.md)

## Derived Classes

[DWGAcadSupportedProxy](../DWGAcadSupportedProxy/DWGAcadSupportedProxy.md), [DWGACMStandardPart](../DWGACMStandardPart/DWGACMStandardPart.md), [DWGArc](../DWGArc/DWGArc.md), [DWGBlockReference](../DWGBlockReference/DWGBlockReference.md), [DWGEllipticalArc](../DWGEllipticalArc/DWGEllipticalArc.md), [DWGEntityProxy](../DWGEntityProxy/DWGEntityProxy.md), [DWGLine](../DWGLine/DWGLine.md), [DWGPoint](../DWGPoint/DWGPoint.md), [DWGPolyline](../DWGPolyline/DWGPolyline.md), [DWGPolyline2D](../DWGPolyline2D/DWGPolyline2D.md), [DWGPolyline3D](../DWGPolyline3D/DWGPolyline3D.md), [DWGSpline](../DWGSpline/DWGSpline.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ImportedDWGComponent Creation](../../sample-programs/ImportedDWGComponentCreation_Sample.md) | This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch. |

## Version

Introduced in version 2016
