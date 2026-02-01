# DerivedFuturePartComponentProxy Object

Derived from: [DerivedFuturePartComponent](../DerivedFuturePartComponent/DerivedFuturePartComponent.md) Object

## Description

DerivedFuturePartComponentProxy object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_Definition.md) | Read-write property that returns the derived future part definition that defines the current state of the derived part.  The state of the derived part can be changed by modifying the values of the returned descriptor and assigning it back to the derived future part using the DerivedFuturePartDefinition property. The part will be updated as a result of the assignment. Note: Definition property will return Nothing if the link to the base part is broken or if the link to the base part could not be resolved. |
| [HealthStatus](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SolidBodies](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_SolidBodies.md) | Read-only property that returns the ReferenceFeature objects that represent the solids that were created as a result of this derived part. |
| [SuppressLinkToFile](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_SuppressLinkToFile.md) | Read-write property that suppresses or unsuppresses the link to the base part. |
| [SurfaceBodies](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_SurfaceBodies.md) | Read-only property that returns the ReferenceFeature objects that represent the work surfaces that were created as a result of this derived part. |
| [Type](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2018
