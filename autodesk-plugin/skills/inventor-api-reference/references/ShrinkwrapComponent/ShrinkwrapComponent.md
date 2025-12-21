# ShrinkwrapComponent Object

Derived from: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md) Object

## Description

The ShrinkwrapComponent object represents a specific shrinkwarp component. This is derived from ReferenceComponent object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ShrinkwrapComponent/ShrinkwrapComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ShrinkwrapComponent/ShrinkwrapComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ShrinkwrapComponent/ShrinkwrapComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ShrinkwrapComponent/ShrinkwrapComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ShrinkwrapComponent/ShrinkwrapComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ShrinkwrapComponent/ShrinkwrapComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../ShrinkwrapComponent/ShrinkwrapComponent_Definition.md) | Gets or Sets ShrinkwrapDefinition that defines the current state of this shrinkwrap component. |
| [HealthStatus](../ShrinkwrapComponent/ShrinkwrapComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ShrinkwrapComponent/ShrinkwrapComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../ShrinkwrapComponent/ShrinkwrapComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../ShrinkwrapComponent/ShrinkwrapComponent_Name.md) | Property that returns the component's name. |
| [Parent](../ShrinkwrapComponent/ShrinkwrapComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../ShrinkwrapComponent/ShrinkwrapComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [ReferenceFeatures](../ShrinkwrapComponent/ShrinkwrapComponent_ReferenceFeatures.md) | Gets the ReferenceFeature objects that were created as a result of this shrinkwrap. |
| [SuppressLinkToFile](../ShrinkwrapComponent/ShrinkwrapComponent_SuppressLinkToFile.md) | Gets and Sets a Boolean flag indicating whether the link to the assembly file is suppressed. |
| [Type](../ShrinkwrapComponent/ShrinkwrapComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ShrinkwrapComponentProxy.NativeObject](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_NativeObject.md), [ShrinkwrapComponents.Add](../ShrinkwrapComponents/ShrinkwrapComponents_Add.md), [ShrinkwrapComponents.Item](../ShrinkwrapComponents/ShrinkwrapComponents_Item.md), [ShrinkwrapDefinition.Parent](../ShrinkwrapDefinition/ShrinkwrapDefinition_Parent.md)

## Derived Classes

[ShrinkwrapComponentProxy](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |