# DerivedPartComponent Object

Derived from: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md) Object

## Description

The DerivedPartComponent object represents a specific derived part instance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedPartComponent/DerivedPartComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedPartComponent/DerivedPartComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedPartComponent/DerivedPartComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Replace](../DerivedPartComponent/DerivedPartComponent_Replace.md) | Replaces current derived part component with another file. |
| [SetEndOfPart](../DerivedPartComponent/DerivedPartComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedPartComponent/DerivedPartComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedPartComponent/DerivedPartComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../DerivedPartComponent/DerivedPartComponent_Definition.md) | Gets the DerivedPartDefinition that defines the current state of the derived part. |
| [HealthStatus](../DerivedPartComponent/DerivedPartComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateDefinitions](../DerivedPartComponent/DerivedPartComponent_iMateDefinitions.md) | Property that returns the iMateDefinition objects that were created as a result of this derived part. |
| [IsEmbedded](../DerivedPartComponent/DerivedPartComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedPartComponent/DerivedPartComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedPartComponent/DerivedPartComponent_Name.md) | Property that returns the component's name. |
| [Parameters](../DerivedPartComponent/DerivedPartComponent_Parameters.md) | Property that returns the Parameter objects that were created as a result of this derived part. This property will return Nothing in the case where the link to the part has been broken. |
| [Parent](../DerivedPartComponent/DerivedPartComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../DerivedPartComponent/DerivedPartComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SketchBlockDefinitions](../DerivedPartComponent/DerivedPartComponent_SketchBlockDefinitions.md) | Property that returns the SketchBlockDefinition objects that were created as a result of this derived part. |
| [SketchBlocks](../DerivedPartComponent/DerivedPartComponent_SketchBlocks.md) | Property that returns the SketchBlock objects that were created as a result of this derived part. |
| [Sketches](../DerivedPartComponent/DerivedPartComponent_Sketches.md) | Property that returns the PlanarSketch objects that were created as a result of this derived part. |
| [Sketches3D](../DerivedPartComponent/DerivedPartComponent_Sketches3D.md) | Property that returns the Sketch3D objects that were created as a result of this derived part. |
| [SolidBodies](../DerivedPartComponent/DerivedPartComponent_SolidBodies.md) | Property that returns the ReferenceFeature objects that represent the solids that were created as a result of this derived part. |
| [SuppressLinkToFile](../DerivedPartComponent/DerivedPartComponent_SuppressLinkToFile.md) | Gets and Sets a Boolean flag indicating whether the link to the part file is suppressed. |
| [SurfaceBodies](../DerivedPartComponent/DerivedPartComponent_SurfaceBodies.md) | Property that returns the SurfaceBody objects that represent work surfaces that were created as a result of this derived part. |
| [Type](../DerivedPartComponent/DerivedPartComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WorkFeatures](../DerivedPartComponent/DerivedPartComponent_WorkFeatures.md) | Property that returns the WorkPlane, WorkAxis, and WorkPoint objects that were created as a result of this derived part. |

## Accessed From

[DerivedPartComponentProxy.NativeObject](../DerivedPartComponentProxy/DerivedPartComponentProxy_NativeObject.md), [DerivedPartComponents.Add](../DerivedPartComponents/DerivedPartComponents_Add.md), [DerivedPartComponents.Item](../DerivedPartComponents/DerivedPartComponents_Item.md)

## Derived Classes

[DerivedPartComponentProxy](../DerivedPartComponentProxy/DerivedPartComponentProxy.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |