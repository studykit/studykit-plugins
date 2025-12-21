# DerivedPartComponentProxy Object

Derived from: [DerivedPartComponent](../DerivedPartComponent/DerivedPartComponent.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedPartComponentProxy/DerivedPartComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedPartComponentProxy/DerivedPartComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedPartComponentProxy/DerivedPartComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Replace](../DerivedPartComponentProxy/DerivedPartComponentProxy_Replace.md) | Replaces current derived part component with another file. |
| [SetEndOfPart](../DerivedPartComponentProxy/DerivedPartComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedPartComponentProxy/DerivedPartComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedPartComponentProxy/DerivedPartComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../DerivedPartComponentProxy/DerivedPartComponentProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../DerivedPartComponentProxy/DerivedPartComponentProxy_Definition.md) | Gets the DerivedPartDefinition that defines the current state of the derived part. |
| [HealthStatus](../DerivedPartComponentProxy/DerivedPartComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateDefinitions](../DerivedPartComponentProxy/DerivedPartComponentProxy_iMateDefinitions.md) | Property that returns the iMateDefinition objects that were created as a result of this derived part. |
| [IsEmbedded](../DerivedPartComponentProxy/DerivedPartComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedPartComponentProxy/DerivedPartComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedPartComponentProxy/DerivedPartComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../DerivedPartComponentProxy/DerivedPartComponentProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parameters](../DerivedPartComponentProxy/DerivedPartComponentProxy_Parameters.md) | Property that returns the Parameter objects that were created as a result of this derived part. This property will return Nothing in the case where the link to the part has been broken. |
| [Parent](../DerivedPartComponentProxy/DerivedPartComponentProxy_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../DerivedPartComponentProxy/DerivedPartComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SketchBlockDefinitions](../DerivedPartComponentProxy/DerivedPartComponentProxy_SketchBlockDefinitions.md) | Property that returns the SketchBlockDefinition objects that were created as a result of this derived part. |
| [SketchBlocks](../DerivedPartComponentProxy/DerivedPartComponentProxy_SketchBlocks.md) | Property that returns the SketchBlock objects that were created as a result of this derived part. |
| [Sketches](../DerivedPartComponentProxy/DerivedPartComponentProxy_Sketches.md) | Property that returns the PlanarSketch objects that were created as a result of this derived part. |
| [Sketches3D](../DerivedPartComponentProxy/DerivedPartComponentProxy_Sketches3D.md) | Property that returns the Sketch3D objects that were created as a result of this derived part. |
| [SolidBodies](../DerivedPartComponentProxy/DerivedPartComponentProxy_SolidBodies.md) | Property that returns the ReferenceFeature objects that represent the solids that were created as a result of this derived part. |
| [SuppressLinkToFile](../DerivedPartComponentProxy/DerivedPartComponentProxy_SuppressLinkToFile.md) | Gets and Sets a Boolean flag indicating whether the link to the part file is suppressed. |
| [SurfaceBodies](../DerivedPartComponentProxy/DerivedPartComponentProxy_SurfaceBodies.md) | Property that returns the SurfaceBody objects that represent work surfaces that were created as a result of this derived part. |
| [Type](../DerivedPartComponentProxy/DerivedPartComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WorkFeatures](../DerivedPartComponentProxy/DerivedPartComponentProxy_WorkFeatures.md) | Property that returns the WorkPlane, WorkAxis, and WorkPoint objects that were created as a result of this derived part. |

## Version

Introduced in version 2008
