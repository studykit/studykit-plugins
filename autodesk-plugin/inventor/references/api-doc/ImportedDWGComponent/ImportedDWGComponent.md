# ImportedDWGComponent Object

Derived from: [ImportedComponent](../ImportedComponent/ImportedComponent.md) Object

## Description

ImportedDWGComponent Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedDWGComponent/ImportedDWGComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ImportedDWGComponent/ImportedDWGComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ImportedDWGComponent/ImportedDWGComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ImportedDWGComponent/ImportedDWGComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedDWGComponent/ImportedDWGComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ImportedDWGComponent/ImportedDWGComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Crop](../ImportedDWGComponent/ImportedDWGComponent_Crop.md) | Read-write property that gets and sets the crop in LocationPlane space. Set this to Nothing will clear the crop. |
| [Definition](../ImportedDWGComponent/ImportedDWGComponent_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [Grounded](../ImportedDWGComponent/ImportedDWGComponent_Grounded.md) | Read-write property that gets and sets whether the object is grounded or not. |
| [HealthStatus](../ImportedDWGComponent/ImportedDWGComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ImportedDWGComponent/ImportedDWGComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [Layers](../ImportedDWGComponent/ImportedDWGComponent_Layers.md) | Read-only property that returns the ImportedDWGLayersEnumerator collection object. |
| [LinkedToFile](../ImportedDWGComponent/ImportedDWGComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [ModelSpaceDefinition](../ImportedDWGComponent/ImportedDWGComponent_ModelSpaceDefinition.md) | Read-only property that returns the DWGModelSpaceDefinition object. |
| [Name](../ImportedDWGComponent/ImportedDWGComponent_Name.md) | Property that returns the component's name. |
| [Origin](../ImportedDWGComponent/ImportedDWGComponent_Origin.md) | Read-only property that returns the work point that represents the origin for the component. |
| [Parent](../ImportedDWGComponent/ImportedDWGComponent_Parent.md) | Property that returns the parent object. |
| [RangeBox](../ImportedDWGComponent/ImportedDWGComponent_RangeBox.md) | Read-only property that returns the bounding box of the DWG graphics. |
| [ReferencedDocumentDescriptor](../ImportedDWGComponent/ImportedDWGComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SuppressLinkToFile](../ImportedDWGComponent/ImportedDWGComponent_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedDWGComponent/ImportedDWGComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ImportedDWGComponent/ImportedDWGComponent_Visible.md) | Read-write property that gets and sets whether this object is visible or not. |
| [XAxis](../ImportedDWGComponent/ImportedDWGComponent_XAxis.md) | Read-only property that returns the work axis that represents the x-axis for the component. |
| [XYPlane](../ImportedDWGComponent/ImportedDWGComponent_XYPlane.md) | Read-only property that returns the work plane that represents the X-Y plane for the component. |
| [XZPlane](../ImportedDWGComponent/ImportedDWGComponent_XZPlane.md) | Read-only property that returns the work plane that represents the X-Z plane for the component. |
| [YAxis](../ImportedDWGComponent/ImportedDWGComponent_YAxis.md) | Read-only property that returns the work axis that represents the y-axis for the component. |
| [YZPlane](../ImportedDWGComponent/ImportedDWGComponent_YZPlane.md) | Read-only property that returns the work plane that represents the Y-Z plane for the component. |
| [ZAxis](../ImportedDWGComponent/ImportedDWGComponent_ZAxis.md) | Read-only property that returns the work axis that represents the z-axis for the component. |

## Accessed From

[DWGAcadSupportedProxy.Parent](../DWGAcadSupportedProxy/DWGAcadSupportedProxy_Parent.md), [DWGAcadSupportedProxyProxy.Parent](../DWGAcadSupportedProxyProxy/DWGAcadSupportedProxyProxy_Parent.md), [DWGACMStandardPart.Parent](../DWGACMStandardPart/DWGACMStandardPart_Parent.md), [DWGACMStandardPartProxy.Parent](../DWGACMStandardPartProxy/DWGACMStandardPartProxy_Parent.md), [DWGArc.Parent](../DWGArc/DWGArc_Parent.md), [DWGArcProxy.Parent](../DWGArcProxy/DWGArcProxy_Parent.md), [DWGBlockDefinition.Parent](../DWGBlockDefinition/DWGBlockDefinition_Parent.md), [DWGBlockDefinitionProxy.Parent](../DWGBlockDefinitionProxy/DWGBlockDefinitionProxy_Parent.md), [DWGBlockReference.Parent](../DWGBlockReference/DWGBlockReference_Parent.md), [DWGBlockReferenceProxy.Parent](../DWGBlockReferenceProxy/DWGBlockReferenceProxy_Parent.md), [DWGEllipticalArc.Parent](../DWGEllipticalArc/DWGEllipticalArc_Parent.md), [DWGEllipticalArcProxy.Parent](../DWGEllipticalArcProxy/DWGEllipticalArcProxy_Parent.md), [DWGEntity.Parent](../DWGEntity/DWGEntity_Parent.md), [DWGEntityProxy.Parent](../DWGEntityProxy/DWGEntityProxy_Parent.md), [DWGEntitySegmentProxy.Parent](../DWGEntitySegmentProxy/DWGEntitySegmentProxy_Parent.md), [DWGLine.Parent](../DWGLine/DWGLine_Parent.md), [DWGLineProxy.Parent](../DWGLineProxy/DWGLineProxy_Parent.md), [DWGPoint.Parent](../DWGPoint/DWGPoint_Parent.md), [DWGPointProxy.Parent](../DWGPointProxy/DWGPointProxy_Parent.md), [DWGPolyline.Parent](../DWGPolyline/DWGPolyline_Parent.md), [DWGPolyline2D.Parent](../DWGPolyline2D/DWGPolyline2D_Parent.md), [DWGPolyline2DProxy.Parent](../DWGPolyline2DProxy/DWGPolyline2DProxy_Parent.md), [DWGPolyline3D.Parent](../DWGPolyline3D/DWGPolyline3D_Parent.md), [DWGPolyline3DProxy.Parent](../DWGPolyline3DProxy/DWGPolyline3DProxy_Parent.md), [DWGPolylineProxy.Parent](../DWGPolylineProxy/DWGPolylineProxy_Parent.md), [DWGSpline.Parent](../DWGSpline/DWGSpline_Parent.md), [DWGSplineProxy.Parent](../DWGSplineProxy/DWGSplineProxy_Parent.md), [DWGUnderlays.Add](DWGUnderlays_Add.md), [DWGUnderlays.Item](DWGUnderlays_Item.md), [ImportedDWGComponentProxy.NativeObject](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_NativeObject.md)

## Derived Classes

[ImportedDWGComponentProxy](../ImportedDWGComponentProxy/ImportedDWGComponentProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ImportedDWGComponent Creation](../../sample-programs/ImportedDWGComponentCreation_Sample.md) | This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |