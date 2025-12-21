# iAssemblyMember Object

## Description

The iAssemblyMember object provides access to a member of an iAssembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFactory](../iAssemblyMember/iAssemblyMember_BreakLinkToFactory.md) | Method that breaks the link to the parent factory and converts the iAssembly member to a regular assembly. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iAssemblyMember/iAssemblyMember_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [HealthStatus](../iAssemblyMember/iAssemblyMember_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [Parent](../iAssemblyMember/iAssemblyMember_Parent.md) | Property that returns the parent AssemblyComponentDefinition of the member. |
| [ParentFactory](../iAssemblyMember/iAssemblyMember_ParentFactory.md) | Property that returns the iAssembly factory that created this iAssemblyMember. |
| [ReferencedDocumentDescriptor](../iAssemblyMember/iAssemblyMember_ReferencedDocumentDescriptor.md) | Property that returns the descriptor of the iAssembly factory document. |
| [Row](../iAssemblyMember/iAssemblyMember_Row.md) | Property that returns the row in the iAssembly table that this iAssemblyMember represents. |
| [Type](../iAssemblyMember/iAssemblyMember_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.iAssemblyMember](../AssemblyComponentDefinition/AssemblyComponentDefinition_iAssemblyMember.md), [WeldmentComponentDefinition.iAssemblyMember](../WeldmentComponentDefinition/WeldmentComponentDefinition_iAssemblyMember.md)

## Version

Introduced in version 11
