# ImportedDWGComponentProxy Object

Derived from: [ImportedDWGComponent](../ImportedDWGComponent/ImportedDWGComponent.md) Object

## Description

ImportedDWGComponentProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Crop](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Crop.md) | Read-write property that gets and sets the crop in LocationPlane space. Set this to Nothing will clear the crop. |
| [Definition](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [Grounded](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Grounded.md) | Read-write property that gets and sets whether the object is grounded or not. |
| [HealthStatus](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [Layers](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Layers.md) | Read-only property that returns the ImportedDWGLayersEnumerator collection object. |
| [LinkedToFile](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [ModelSpaceDefinition](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_ModelSpaceDefinition.md) | Read-only property that returns the DWGModelSpaceDefinition object. |
| [Name](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Origin](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Origin.md) | Read-only property that returns the work point that represents the origin for the component. |
| [Parent](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Parent.md) | Property that returns the parent object. |
| [RangeBox](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_RangeBox.md) | Read-only property that returns the bounding box of the DWG graphics. |
| [ReferencedDocumentDescriptor](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SuppressLinkToFile](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Visible.md) | Read-write property that gets and sets whether this object is visible or not. |
| [XAxis](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_XAxis.md) | Read-only property that returns the work axis that represents the x-axis for the component. |
| [XYPlane](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_XYPlane.md) | Read-only property that returns the work plane that represents the X-Y plane for the component. |
| [XZPlane](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_XZPlane.md) | Read-only property that returns the work plane that represents the X-Z plane for the component. |
| [YAxis](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_YAxis.md) | Read-only property that returns the work axis that represents the y-axis for the component. |
| [YZPlane](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_YZPlane.md) | Read-only property that returns the work plane that represents the Y-Z plane for the component. |
| [ZAxis](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_ZAxis.md) | Read-only property that returns the work axis that represents the z-axis for the component. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |