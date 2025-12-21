# iPartMember Object

Derived from: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md) Object

## Description

The iPartMember object provides access to the iPart.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFactory](../iPartMember/iPartMember_BreakLinkToFactory.md) | Method that breaks the link to the parent factory and converts the iPart member to a derived part. |
| [BreakLinkToFile](../iPartMember/iPartMember_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [ChangeRow](../iPartMember/iPartMember_ChangeRow.md) | Method that changes the row in the iPartTable that this custom iPartMember represents. This method is only valid for custom members. This can be determined using the CustomMember property. |
| [Delete](../iPartMember/iPartMember_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../iPartMember/iPartMember_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../iPartMember/iPartMember_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iPartMember/iPartMember_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../iPartMember/iPartMember_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CustomMember](../iPartMember/iPartMember_CustomMember.md) | Property that specifies whether this iPartMember represents a custom member or a standard member. This property is True if the iPartMember is a CustomMember. |
| [HealthStatus](../iPartMember/iPartMember_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../iPartMember/iPartMember_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../iPartMember/iPartMember_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../iPartMember/iPartMember_Name.md) | Property that returns the component's name. |
| [Parent](../iPartMember/iPartMember_Parent.md) | Property that returns the parent object. |
| [ParentFactory](../iPartMember/iPartMember_ParentFactory.md) | Property that returns the iPart factory that created this iPartMember. |
| [PrimaryBody](../iPartMember/iPartMember_PrimaryBody.md) | Property that returns the primary body as a solid body. The solid body corresponds to the resultant body obtained from the iPartFactory. |
| [ReferencedDocumentDescriptor](../iPartMember/iPartMember_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [Row](../iPartMember/iPartMember_Row.md) | Property that returns the row in the iPart table that this iPartMember represents. |
| [Type](../iPartMember/iPartMember_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iPartFactory.CreateCustomMember](../iPartFactory/iPartFactory_CreateCustomMember.md), [iPartFactory.CreateMember](../iPartFactory/iPartFactory_CreateMember.md), [PartComponentDefinition.iPartMember](../PartComponentDefinition/PartComponentDefinition_iPartMember.md), [SheetMetalComponentDefinition.iPartMember](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_iPartMember.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |