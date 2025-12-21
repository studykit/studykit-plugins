# ImportedGenericComponent Object

Derived from: [ImportedComponent](../ImportedComponent/ImportedComponent.md) Object

## Description

ImportedGenericComponent Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedGenericComponent/ImportedGenericComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ImportedGenericComponent/ImportedGenericComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ImportedGenericComponent/ImportedGenericComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ImportedGenericComponent/ImportedGenericComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedGenericComponent/ImportedGenericComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ImportedGenericComponent/ImportedGenericComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../ImportedGenericComponent/ImportedGenericComponent_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [HealthStatus](../ImportedGenericComponent/ImportedGenericComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ImportedGenericComponent/ImportedGenericComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../ImportedGenericComponent/ImportedGenericComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../ImportedGenericComponent/ImportedGenericComponent_Name.md) | Property that returns the component's name. |
| [Parent](../ImportedGenericComponent/ImportedGenericComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../ImportedGenericComponent/ImportedGenericComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SuppressLinkToFile](../ImportedGenericComponent/ImportedGenericComponent_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedGenericComponent/ImportedGenericComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ImportedGenericComponentProxy.NativeObject](../ImportedGenericComponentProxy/ImportedGenericComponentProxy_NativeObject.md)

## Derived Classes

[ImportedGenericComponentProxy](../ImportedGenericComponentProxy/ImportedGenericComponentProxy.md)

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |