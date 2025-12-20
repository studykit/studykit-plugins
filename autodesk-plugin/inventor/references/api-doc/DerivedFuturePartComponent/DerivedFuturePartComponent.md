# DerivedFuturePartComponent Object

Derived from: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md) Object

## Description

The DerivedFuturePartComponent object represents a specific derived future part instance. This is derived from ReferenceComponent object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedFuturePartComponent/DerivedFuturePartComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedFuturePartComponent/DerivedFuturePartComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedFuturePartComponent/DerivedFuturePartComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../DerivedFuturePartComponent/DerivedFuturePartComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedFuturePartComponent/DerivedFuturePartComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedFuturePartComponent/DerivedFuturePartComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../DerivedFuturePartComponent/DerivedFuturePartComponent_Definition.md) | Read-write property that returns the derived future part definition that defines the current state of the derived part.  The state of the derived part can be changed by modifying the values of the returned descriptor and assigning it back to the derived future part using the DerivedFuturePartDefinition property. The part will be updated as a result of the assignment. Note: Definition property will return Nothing if the link to the base part is broken or if the link to the base part could not be resolved. |
| [HealthStatus](../DerivedFuturePartComponent/DerivedFuturePartComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../DerivedFuturePartComponent/DerivedFuturePartComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedFuturePartComponent/DerivedFuturePartComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedFuturePartComponent/DerivedFuturePartComponent_Name.md) | Property that returns the component's name. |
| [Parent](../DerivedFuturePartComponent/DerivedFuturePartComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../DerivedFuturePartComponent/DerivedFuturePartComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SolidBodies](../DerivedFuturePartComponent/DerivedFuturePartComponent_SolidBodies.md) | Read-only property that returns the ReferenceFeature objects that represent the solids that were created as a result of this derived part. |
| [SuppressLinkToFile](../DerivedFuturePartComponent/DerivedFuturePartComponent_SuppressLinkToFile.md) | Read-write property that suppresses or unsuppresses the link to the base part. |
| [SurfaceBodies](../DerivedFuturePartComponent/DerivedFuturePartComponent_SurfaceBodies.md) | Read-only property that returns the ReferenceFeature objects that represent the work surfaces that were created as a result of this derived part. |
| [Type](../DerivedFuturePartComponent/DerivedFuturePartComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedFuturePartComponentProxy.NativeObject](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_NativeObject.md), [DerivedFuturePartComponents.Add](../DerivedFuturePartComponents/DerivedFuturePartComponents_Add.md), [DerivedFuturePartComponents.Item](../DerivedFuturePartComponents/DerivedFuturePartComponents_Item.md)

## Derived Classes

[DerivedFuturePartComponentProxy](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |