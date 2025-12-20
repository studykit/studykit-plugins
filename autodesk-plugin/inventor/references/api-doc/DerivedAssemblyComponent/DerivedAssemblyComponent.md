# DerivedAssemblyComponent Object

Derived from: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md) Object

## Description

The DerivedAssemblyComponent object represents a specific derived assembly instance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedAssemblyComponent/DerivedAssemblyComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedAssemblyComponent/DerivedAssemblyComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedAssemblyComponent/DerivedAssemblyComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Replace](../DerivedAssemblyComponent/DerivedAssemblyComponent_Replace.md) | Replaces current derived assembly component with another file. |
| [SetEndOfPart](../DerivedAssemblyComponent/DerivedAssemblyComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedAssemblyComponent/DerivedAssemblyComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedAssemblyComponent/DerivedAssemblyComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../DerivedAssemblyComponent/DerivedAssemblyComponent_Definition.md) | Gets or sets DerivedAssemblyDefinition that defines the current state of this derived assembly. |
| [HealthStatus](../DerivedAssemblyComponent/DerivedAssemblyComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../DerivedAssemblyComponent/DerivedAssemblyComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedAssemblyComponent/DerivedAssemblyComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedAssemblyComponent/DerivedAssemblyComponent_Name.md) | Property that returns the component's name. |
| [Parent](../DerivedAssemblyComponent/DerivedAssemblyComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../DerivedAssemblyComponent/DerivedAssemblyComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [ReferenceFeatures](../DerivedAssemblyComponent/DerivedAssemblyComponent_ReferenceFeatures.md) | Property that returns the collection containing the ReferenceFeatures that was created as a result of the derived component. |
| [SuppressAll](../DerivedAssemblyComponent/DerivedAssemblyComponent_SuppressAll.md) | Property that gets and sets the suppress state for all of the Reference features created by this derived assembly component. |
| [SuppressLinkToFile](../DerivedAssemblyComponent/DerivedAssemblyComponent_SuppressLinkToFile.md) | Gets and Sets a Boolean flag indicating whether the link to the assembly file is suppressed. |
| [Type](../DerivedAssemblyComponent/DerivedAssemblyComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedAssemblyComponentProxy.NativeObject](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_NativeObject.md), [DerivedAssemblyComponents.Add](../DerivedAssemblyComponents/DerivedAssemblyComponents_Add.md), [DerivedAssemblyComponents.Item](../DerivedAssemblyComponents/DerivedAssemblyComponents_Item.md)

## Derived Classes

[DerivedAssemblyComponentProxy](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |